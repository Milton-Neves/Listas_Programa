from smtplib import SMTP_SSL
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from time import sleep

def send_message(email, name, html):
    with SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(email, 'Lalala1.2')

        msg = MIMEMultipart()
        msg['Subject'] = 'E-mail enviado com sucesso'
        msg['From'] = 'milzonzneves@gmail.com'
        msg['To'] = 'questaoquatro@gmail.com'
        html = MIMEText(html, 'html')
        msg.attach(html)

        text = msg.as_string()

        server.send_message(msg ['From'], msg ['To'], text ['Subject'])
        print(f"Email enviado para: {name}")
        sleep(2)
