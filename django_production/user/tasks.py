from django_production.celery import app
from django.core.mail import mail_managers

@app.task
def send_email_task():
    """ This function sends an email to Mayer & Co collaborateurs
    """
    mail_managers(subject="Test V3 from Django production", message="Message de test de django production avec Celery")
    return True
