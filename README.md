# Keylogger Program

This is a basic keylogger implemented in Python using the `pynput` library. It records all keystrokes and saves them to a log file.

## Features
- Logs all keys pressed by the user.
- Records special keys like space, enter, backspace, etc., and stores them in a readable format.
- Saves the logs to a file (`key_log.txt`).
- Stops recording when the `esc` key is pressed.

## Installation
1. Install the required library `pynput`:
   ```bash
   pip install pynput
