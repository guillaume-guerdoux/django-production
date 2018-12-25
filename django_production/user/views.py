from django.shortcuts import render
from user.tasks import send_email_task
from django.core.mail import mail_managers

def send_email(request):
    print('EMAIL SENT')
    # send_email_task.delay()
    mail_managers(subject="Test from Django production", message="Message de test de django production avec Celery")
    return render(request, 'home.html')
