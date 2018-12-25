import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_production.settings')

app = Celery('django_production')
app.config_from_object('django.conf:settings')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

@app.task(name='celery.ping')
def ping():
    # type: () -> str
    """Simple task that just returns 'pong'."""
    return 'pong'
