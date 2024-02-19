import pyautogui

# Use the confirm function to display a message box with "OK" and "Cancel" buttons
pyautogui.confirm('Your program is Cool.')

# Use the alert function to display an error message box with a custom title and "OK" button
pyautogui.alert('ERROR: No button found.', 'ERROR', 'OK')

# Use the prompt function to display a message box with a text input field
pyautogui.prompt('Please enter your name:')

# Use the password function to display a message box with a password input field
pyautogui.password('Enter your password:')

