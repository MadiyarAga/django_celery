import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.conf import settings


def send_email_task(recipient, subject, message):
    """Функция отправки email через SMTP."""

    msg = MIMEMultipart()
    msg['From'] = settings.EMAIL_HOST_USER
    msg['To'] = recipient
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'simple'))

    try:
        with smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT) as server:
            server.starttls()
            server.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
            server.sendmail(settings.EMAIL_HOST_USER, recipient, msg.as_string())
    except Exception as e:
        print(f"Ошибка отправки email: {e}")


def log_email(recipient, subject, message):
    """Логирование отправленного email."""

    with open('email_log.txt', "a", encoding="utf-8") as f:
        f.write(f"To: {recipient} \nSubject: {subject} \nMessage: {message}\n\n")

    print(f"Email отправлен: {recipient}, Тема: {subject}, Сообщение: {message}")
