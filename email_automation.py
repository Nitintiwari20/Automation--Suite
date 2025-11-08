# email_automation.py
import smtplib
from email.mime.text import MIMEText

def send_email(subject, body, to_email):
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = "20nitin9tiwari2005@gmail.com"
    msg["To"] = to_email

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login("20nitin9tiwari2005@gmail.com", "up03a65743")
        server.send_message(msg)