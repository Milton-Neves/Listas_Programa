from smtplib import SMTP_SSL
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from time import sleep

def send_message(email, name, html):
    with SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(email, password)

        msg = MIMEMultipart()
        msg['Subject'] = SUBJECT
        msg['From'] = email_de
        msg['To'] = email_para
        html = MIMEText(html, 'html')
        msg.attach(html)

        text = msg.as_string()

        server.send_message(msg, text)
        print(f"Email enviado para: {name}")
        sleep(2)
