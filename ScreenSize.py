# Description: This script will print the size of the computer screen in pixels (width, height).

import pyautogui

# Get the size of the computer screen in pixels (width, height)
screen_size = pyautogui.size()

# Print the screen size
print(f"Screen size: {screen_size}")