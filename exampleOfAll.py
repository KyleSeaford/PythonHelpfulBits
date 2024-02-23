import pyautogui

name = pyautogui.prompt('Please enter your name:', default= 'Kyle Seaford')
password = pyautogui.password('Enter your password:', default='password123')

pyautogui.alert('Name: ' + name + '\nPassword: ' + password , 'Your Information', 'OK')
