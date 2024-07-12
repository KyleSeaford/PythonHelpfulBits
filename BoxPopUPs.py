# Description: This script demonstrates how to use the confirm, alert, prompt, and password functions in the PyAutoGUI library to display message boxes with different types of input fields and buttons.

import pyautogui

# Use the confirm function to display a message box with "OK" and "Cancel" buttons
pyautogui.confirm('Your program is Cool.')

# Use the alert function to display an error message box with a custom title and "OK" button
pyautogui.alert('ERROR: No button found.', 'ERROR', 'OK')

# Use the prompt function to display a message box with a text input field
pyautogui.prompt('Please enter your name:')

# Use the password function to display a message box with a password input field
pyautogui.password('Enter your password:')


# an example of using the confirm function with custom buttons, i dont know why its called deepthoughts, but it is

buttons = pyautogui.confirm('Your program is Cool.', 'deepthoughts', buttons=['Yes', 'No', 'Cancel'])

if buttons == 'Yes':
    pyautogui.alert('You are cool', 'deepthoughts', 'OK')
elif buttons == 'No':
    pyautogui.alert('You are not cool', 'deepthoughts', 'OK')
else:
    pyautogui.alert('You are undecided', 'deepthoughts', 'OK')


# an example of using the prompt function with a default value
    
name = pyautogui.prompt('Please enter your name:', default= 'Kyle Seaford')
password = pyautogui.password('Enter your password:', default='password123')

pyautogui.alert('Name: ' + name + '\nPassword: ' + password , 'Your Information', 'OK')
