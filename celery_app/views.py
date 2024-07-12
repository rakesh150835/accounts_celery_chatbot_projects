from django.http import JsonResponse

from .tasks import add_two_num, send_email_task


def send_email_view(request):
    subject = 'Hello from Celery'
    message = 'This is a test email sent asynchronously with Celery.'
    recipient_list = ['rakesh@snakescript.com']
    send_email_task.delay(subject, message, recipient_list)
    return 



def your_view(request):
    # Call the asynchronous task using delay() method
    task_result = add_two_num.delay(10, 20)
    return JsonResponse({'task_id': task_result.id})







