**Overview**


This simple keylogger program captures keystrokes and logs them to a text file (keylog.txt). It uses the pynput library to listen for keyboard input and records every key pressed until the escape key (Esc) is pressed to stop the program.

**How It Works**

- Keystroke Capture: The program listens for keyboard events. It logs each key pressed, whether it's a character key or a special key (like Enter or Space).
- File Logging: All captured keystrokes are saved in a file named keylog.txt in the same directory as the script.
- User Input: The keylogger runs in the background and captures all keystrokes until you press Esc to terminate the logging session.
- Output: The captured keystrokes are saved in the keylog.txt file, which you can review to see the recorded input.

**Usage Example**

1. Install the necessary library with the command: pip install pynput.
2. Run the program.
3. The keylogger will start capturing keystrokes and save them to keylog.txt.
4. Press Esc to stop the program.
5. Open keylog.txt to view the captured keystrokes.
