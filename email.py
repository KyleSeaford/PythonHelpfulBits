import smtplib
from email.mime.text import MIMEText
import datetime

def sendlogTOkyle():
    now = datetime.datetime.now()

    sender = 'contact@kyle-seaford.co.uk' # email address
    receivers = ['projects@kyle-seaford.co.uk'] # recipient email address
    # email deatails for sender account
    smtp_server = 'smtp.ionos.co.uk' 
    smtp_port = 587
    smtp_username = '' # email address
    smtp_password = '' # email password

    # Build the message with MIMEText for proper formatting
    message = MIMEText(f"email at {now}")
    message['Subject'] = f"subject gose here"
    message['From'] = sender
    message['To'] = ', '.join(receivers)

    try:
        smtpObj = smtplib.SMTP(smtp_server, smtp_port)
        smtpObj.starttls()  
        
        smtpObj.login(smtp_username, smtp_password)
        
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("Successfully sent email")
    except smtplib.SMTPException as e:
        print(f"Error: {e}")
