from .celery import app
from account.send_email import send_confirmation_email
from django.core.mail import send_mail


@app.task
def send_email_task(user,code):
    send_confirmation_email(user,code)

