import requests
from celery import shared_task

from .utils import send_email_task, log_email
# from send_email.celery import app
# from main.service import send


@shared_task
def send_spam_email(recipient, subject, message):
    print(f"Email отправлен: {recipient}, Тема: {subject}, Сообщение: {message}")

    send_email_task(recipient, subject, message)
    log_email(recipient, subject, message)


# @app.task
# def write_file(email):
#     send(email)
#     return True
#
#
# @app.task
# def get_api():
#     response = requests.get('https://api.publicapis.org/categories')
#     if response.status_code == 200:
#         save_categories(response.json())
#         return True
#     return False
#
#
# @app.task
# def test_task():
#     print('Its Worked')
#     return True
