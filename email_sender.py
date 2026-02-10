import smtplib
from email.message import EmailMessage

from secrets import EMAIL_ADDRESS, RECEIVER_EMAIL, EMAIL_PASSWORD

def send_email(RECEIVER_EMAIL: str, subject: str, content: str) -> str:
    """ Send an email to the specified receiver."""
    msg = EmailMessage()
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = RECEIVER_EMAIL
    msg["Subject"] = "Hello from Python 🐍"

    msg.set_content(content)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)

    print("Email sent successfully!")
    return "Email sent successfully!"

