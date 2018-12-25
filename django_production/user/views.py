from django.shortcuts import render
from user.tasks import send_email_task
from django.core.mail import mail_managers

def send_email(request):
    print('EMAIL SENT')
    send_email_task.delay()
    return render(request, 'home.html')
