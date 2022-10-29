import smtplib
from email.message import EmailMessage
from email_settings import password, my_mail


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



