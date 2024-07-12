# description: This script demonstrates how to simulate mouse movements using the pyautogui module.

import pyautogui

# Move the mouse to the specified x and y coordinates
# The duration argument specifies the time in seconds to complete the movement
pyautogui.moveTo(100, 100, duration=1)

# Drag the mouse from the current position to the specified x and y coordinates
# The duration argument specifies the time in seconds to complete the dragging
pyautogui.dragTo(100, 100, duration=1)

# Scroll the mouse wheel by the specified number of lines
# A positive number scrolls down, a negative number scrolls up
pyautogui.scroll(200)

# Scroll the mouse wheel by the specified number of lines
# A positive number scrolls down, a negative number scrolls up
pyautogui.scroll(-200)