import pyautogui

# Use the confirm function to display a message box with "OK" and "Cancel" buttons
confirmation_result = pyautogui.confirm('Your program is Cool.')
print("Confirmation Result:", confirmation_result)

# Use the alert function to display an error message box with a custom title and "OK" button
pyautogui.alert('ERROR: No button found.', 'ERROR', 'OK')
print("Alert displayed.")

# Use the prompt function to display a message box with a text input field
user_input = pyautogui.prompt('Please enter your name:')
print("User input:", user_input)

# Use the password function to display a message box with a password input field
user_password = pyautogui.password('Enter your password:')
print("User password:", user_password)
