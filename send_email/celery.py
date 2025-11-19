import os
from celery import Celery
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'send_email.settings')

app = Celery('send_email')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


# celety beat tasks

app.conf.beat_schedule = {
    'send-spam-every-3-minute': {
        'task': 'main.tasks.send_beat_email',
        'schedule': crontab(minute='*/3'),
    },
}
