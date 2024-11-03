import smtplib
import ssl
import os


def send_email(message):
    host = 'smtp.gmail.com'
    port = 465
    user_name = 'nenad.rosoman@gmail.com'
    password = 'bbxqirltgzbaxghn'
    context = ssl.create_default_context()
    receiver = 'nenad.andonov@yahoo.com'

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(user_name, password)
        server.sendmail(user_name, receiver, message)


print(os.getenv('PASSWORD'))
