from celery import shared_task
from blog_project.celery import app
from django.core.mail import send_mail


@app.task
def send_email_task(subject, message, sender, recipient_list):
    send_mail(subject, message, sender, recipient_list)




@app.task
def add_two_num(arg1, arg2):
    result = arg1 + arg2
    print("result: ", result)
    return result


@app.task
def my_periodic_task():
    print("This is a periodic task. It will run after specified time interval.")
