import json
import pyautogui
import time
import keyboard

# Load commands from JSON file
print("Press F1 to start pasting commands, and press CTRL+C to exit.")
with open('commands.json', 'r') as file:
    commands_json = json.load(file)

# Set typing speed (adjust this value as needed)
typing_speed = 0.001  # seconds per character

# Flag to keep track of whether typing is in progress
typing_in_progress = False

def type_commands():
    global typing_in_progress
    typing_in_progress = True
    for command in commands_json:
        pyautogui.write(command, interval=typing_speed)
        pyautogui.press('enter')
        time.sleep(0.7)  # Wait between sending commands (adjust as needed)
    typing_in_progress = False

# Function to handle F1 key press
def on_press_F1(event):
    print("F1 pressed. Starting typing...")
    type_commands()

# Register the F1 key event
keyboard.on_press_key("f1", on_press_F1)

# Keep the script running
keyboard.wait('esc')  # Wait for Esc key to exit gracefully
