# Import the pyautogui module, which allows us to interact with the screen and mouse
import pyautogui

# Move the mouse to the specified x and y coordinates
# The duration argument specifies the time in seconds to complete the movement
pyautogui.moveTo(100, 100, duration=1)

# Drag the mouse from the current position to the specified x and y coordinates
# The duration argument specifies the time in seconds to complete the dragging
pyautogui.dragTo(100, 100, duration=1)