from django.test import TestCase
from main.tasks import send_email_task, log_email
import os


class EmailTaskTests(TestCase):
    def test_log_email(self):
        recipient = "test@example.com"
        subject = "Тест. no-reply"
        message = "Это сообщение является тестовым!"

        log_email(recipient, subject, message)

        with open("email_log.txt", "r", encoding="utf-8") as f:
            content = f.read()

        self.assertIn(recipient, content)
        self.assertIn(subject, content)
        self.assertIn(message, content)

    def test_send_email_task(self):
        recipient = "test@example.com"
        subject = "Тест. no-reply"
        message = "Это сообщение является тестовым!"

        try:
            send_email_task(recipient, subject, message)
        except Exception as e:
            self.fail(f"send_email_task вызвала исключение: {e}")
