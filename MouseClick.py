# Import the pyautogui module, which allows us to interact with the screen and mouse
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