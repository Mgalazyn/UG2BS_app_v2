import smtplib
from email.message import EmailMessage

from dotenv import load_dotenv
import os
from build_workout import build_workout


load_dotenv()
my_mail = os.getenv("my_mail")
password = os.getenv("password")


def send_email(message, subject='Your workout for today',
               server='smtp.gmail.com',
               from_email=my_mail):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = input('Type in your email: '),
    msg.set_content(message)
    server = smtplib.SMTP(server, 587)
    server.ehlo()
    server.starttls()
    server.login(from_email, password)
    server.send_message(msg)
    server.quit()
    print('Workout send successfully')


print(send_email(message=str(build_workout())))


