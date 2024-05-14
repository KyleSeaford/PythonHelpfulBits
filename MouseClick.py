# Description: This script demonstrates how to perform a left click, right click, double click, and click at a specific x and y coordinate using the PyAutoGUI library.

import pyautogui

# Perform a left click at the current mouse position
pyautogui.click()

# Perform a right click at the current mouse position
pyautogui.click(button='right')

# Perform a left click at the specified x and y coordinates
pyautogui.click(100, 100)

# Perform a right click at the specified x and y coordinates
pyautogui.click(100, 100, button='right')

# Perform a double left click at the current mouse positioN
pyautogui.doubleClick()

# Perform a double right click at the current mouse position
pyautogui.doubleClick(100, 100)