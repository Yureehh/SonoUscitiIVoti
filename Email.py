import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import ssl
import os
from dotenv import load_dotenv



# User configuration
sender_email = os.environ.get('Email_Uni_Google')
mymail = os.environ.get('Email_Uni')
maildonno = os.environ.get('Email_Uni_Donno')
receivers_email = [mymail]#, maildonno]
password = os.environ.get('Unicorni')
subject = "Voti"


# Email text
email_body = '''
    Sono usciti i voti
'''

def send_mail():
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["Subject"] = subject

    for receiver in receivers_email:

        msg["To"] = receiver

        msg.attach(MIMEText(email_body, 'plain'))

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, password)
        text = msg.as_string()
        server.sendmail(sender_email, receiver, text)
        server.quit()

if __name__ =='__main__':
    send_mail()