from celery import shared_task
from django.core.mail import send_mail
from send_email.celery import app

from .models import Contact
from .service import send


@app.task
def send_spam_email(user_email):
    send(user_email)


@app.task
def send_beat_emial():
    for contact in Contact.objects.all():
        send_mail(
            'Вы подписались на рассылку',
            'Мы будем присылать Вам много спама каждые 5 минут.',
            'djangocelery@gmail.com',
            [contact.email],
            fail_silently=False,
        )


# @app.task
# def my_task(a, b):
#     return a + b
#
#
# @app.task(bind=True, default_retry_delay=5 * 60)
# def my_task_retry(self, x, y):
#     try:
#         return x + y
#     except Exception as exc:
#         raise self.retry(exc=exc, countdown=60)
#
#
# @shared_task
# def my_shared_task(msg):
#     return msg + '!!!'
