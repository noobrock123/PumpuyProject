import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PumpuyProject.settings')
app = Celery('PumpuyProject')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

def debug_task(self):
    print(f'Request: {self.request!r}')