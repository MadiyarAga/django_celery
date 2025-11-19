celery_app = "send_email"

host = 'localhost'
port = 5555

broker_url = 'redis://localhost:6379/0'

auto_refresh = True
refresh_interval = 5

logging = 'info'
