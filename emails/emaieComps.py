# Purpose: Send emails to companies in the companies dictionary

import smtplib
import time
from email.mime.text import MIMEText

# Define a dictionary of companies

# test companies dictionary, change to companies2 to companies to send to test emails
companies2 = {
    "company1": {"name": "Company 1", "email": "projects@kyle-seaford.co.uk", "focus": "focus1"},
    "company2": {"name": "Company 2", "email": "kyleseaford5@gmail.com", "focus": "focus2"},
}

# real companies dictionary, change to companies to companies2 to send the test emails 
companies = {
    "company1": {"name": "Pecometer Software", "email": "enquiries@pecometer.co.uk", "focus": "Bespoke Software Development"},
    "company3": {"name": "Peak", "email": "info@peak.ai", "focus": "AI SaaS development"},
    "company4": {"name": "RevGlue", "email": "support@revglue.com", "focus": "SaaS Monetisation Tools"},
    "company5": {"name": "CultureAI", "email": "contact@culture.ai", "focus": "Human Security and AI"},
    "company6": {"name": "LocalLinkk", "email": "projects@kyle-seaford.co.uk", "focus": "Data Science, AI and connecting people together"},

}

# Define a dictionary of companies with websites
websites = {
    "company2": "https://www.pecometer.co.uk",
    "company5": "https://www.peak.ai",
    "company6": "https://www.revglue.com",
    "company7": "https://www.culture.ai",

    "company8": "https://www.locallinkk.tech"}



# Define email content
mail_template = """\

Dear {name} Team,

My name is Kyle Seaford, and I am interested in gaining work experience at your company.

I am an adaptable and enthusiastic individual with a sincere passion for computer technology. I believe that my drive for learning and staying updated on the latest trends,
aligns well with {name}'s focus in {focus}. I am aspiring to be a data scientist / software engineer, and I believe that the work being done at {name} would provide me with valuable hands-on experience in this field.

I would greatly appreciate the opportunity to work with your dynamic team and gain practical experience in data science / software engineering.
Please let me know if there are any available work experience or different opportunities at {name}.

Feel free to ask any questions, my LinkedIn is attached, Sincerely Kyle Seaford.
https://www.linkedin.com/in/kyle-seaford/

"""

# Define email details

sender = 'contact@kyle-seaford.co.uk'

smtp_server = 'smtp.ionos.co.uk'

smtp_port = 587

smtp_username = 'contact@kyle-seaford.co.uk'

smtp_password = 'Ks_contact123'

# Iterate over companies
for name, details in companies.items():

    print(f"Processing email for {details['name']}")

    # Create email message

    mail = mail_template.format(name=details['name'], focus=details['focus'])

    message = MIMEText(mail)

    message['Subject'] = "Work Experience Inquiry: Kyle Seaford"

    message['From'] = sender

    message['To'] = details['email']

    # Send email

    try:
        smtpObj = smtplib.SMTP(smtp_server, smtp_port)

        smtpObj.starttls()

        smtpObj.login(smtp_username, smtp_password)

        smtpObj.sendmail(sender, [details['email']], message.as_string())

        print(f"Successfully sent email to {details['name']}")

    except smtplib.SMTPException as e:
        print(f"Error: {e}")

    print(f"Finished processing email for {details['name']}\n")
    time.sleep(2)