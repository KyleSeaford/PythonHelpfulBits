# Import the pyautogui module, which allows us to interact with the screen and mouse
import pyautogui
# import the time module, which allows us to add delays to our code
import time

# Type a string 
pyautogui.typewrite('Hello world!')

# Type a string with a 0.1 second delay between each character
pyautogui.typewrite('Hello world!', interval=0.1)

# Press a key on the keyboard
pyautogui.press('enter')

# Press a key combination
pyautogui.hotkey('ctrl', 'c')

# Press a key and hold it down
pyautogui.keyDown('shift')
time.sleep(1)  # wait for 1 second
pyautogui.keyUp('shift')


# Press a key combination and hold it down
pyautogui.hotkey('ctrl', 'alt', 'del')


# The following keys are supported:

#'  \t', '\n', '\r', ' ', '!', '"', '#', '$', '%', '&', "'", '(',
#   ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7',
#   '8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`',
#   'a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
#   'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~',
#   'accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace',
#   'browserback', 'browserfavorites', 'browserforward', 'browserhome',
#   'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear',
#   'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete',
#   'divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10',
#   'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20',
#   'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9',
#   'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja',
#   'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail',
#   'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack',
#   'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6',
#   'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn',
#   'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn',
#   'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator',
#   'shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab',
#   'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen',
#   'command', 'option', 'optionleft', 'optionright'
