import os
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv

# .env dosyasını yükle
load_dotenv("smtp_config.env")

SMTP_HOST = os.getenv("SMTP_HOST")
SMTP_PORT = int(os.getenv("SMTP_PORT"))
SMTP_USER = os.getenv("SMTP_USER")
SMTP_PASS = os.getenv("SMTP_PASS")
MAIL_FROM = os.getenv("MAIL_FROM")
MAIL_REPLY_TO = os.getenv("MAIL_REPLY_TO")

def send_mail(to_email, subject, body):
    msg = MIMEText(body, "plain", "utf-8")
    msg["Subject"] = subject
    msg["From"] = MAIL_FROM
    msg["To"] = to_email
    msg["Reply-To"] = MAIL_REPLY_TO

    try:
        with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USER, SMTP_PASS)
            server.sendmail(MAIL_FROM, [to_email], msg.as_string())

        print("Mail başarıyla gönderildi")

    except Exception as e:
        print("Mail gönderilirken hata:", e)


if __name__ == "__main__":
    send_mail(
        "test@example.com",
        "Test Mail",
        "Bu mail SMTP konfigürasyon testidir."
    )
