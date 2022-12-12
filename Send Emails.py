import smtplib
import ssl
from email.message import EmailMessage

# Define email sender and receiver
email_sender = 'songicooper@gmail.com'
email_password = 'write-sender-password-here'
email_receiver = 'coopercodes101@gmail.com'

# Set the subject and body of the email
subject = 'Automating emails with python'
body = """
this email was sent using automation process by hellosongi
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

# Add SSL (layer of security)
context = ssl.create_default_context()

# Log in and send the email
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
