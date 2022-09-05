# Keylogger_Python
This is the keylogger project made using various libraries of python such as pynput , scipy , soundtrack , win32 etc. It is the advanced version of the keylogger this keylogger is capable of recording audio using microphones , Capturing the screenshots , Gathering all the computer informations  regarding processors and the operating system that the sytem is using , It can mail all the gained information to the base or the attacker.

Packages Used:
These can also be considered as the requirements that is required to be installed to run this project
- pywin32
- pynput
- scipy
- cryptography
- requests
- pillow
- sounddevice

Important funtions  that are present inside this projects:

- On_press(Key):
  This works as the listner function that will listen for the key strokes that the victim will enter.
  This uses the Key module of the pynput.
  
- write_file(key):
  This function is basically used to write the keystrokes into the file and later these files will be used as attachment to the gmail which is sent to the base.
  
- On_release(key):
  This is the another listner which will listen to the specific key after getting that particular keystroke the keylogger will exit in our case this is escape key.
  
- send_email():
  This is the function that is responsible for sending the email . The email contains the keystrokes as well as the additional attachments which are the system info the voice 
  that is recorded by the keylogger and the snaps that is taken by the keylogger.
  
- computer_information():
  This is the function that is used to gather the information about your computer the informations are:
      - Private ip address
      - Public ip address
      - Processor information
      - Platform information
        - OS Name 
        - OS Version
      - Platform hostname
 
- microphone():
  This is the function that will be used to record the audio from the victims computer.
  This is the advanced feature for a microphone.
 
- copy_clipboard():
  This function is used to copy the information that will be stored inside the clipboard of the system.
  
- Screenshot():
  This function captures the screenshot from the victims computer using the Imagegrab from the Pillow library.
  

we use the encryption algorithm to encrypt the keystrokes so that the victim could not understand the original intent as he will be seeing the random alphbets.

Files:-

- Decryptfile.py:
  This file will be used to decrypt the file which is recevied from the victims computer to get the accurate keystrokes.
  This uses the cryptography.fermat module

- Generatekey.py
  This is the file that will be used to generate the key which will be used for the encryption and the decryption purpose.
  
- Keylogger.py
  This is the original file where the keylogger project is stored and all the functions related to the keylogger project is stored.
  

  

