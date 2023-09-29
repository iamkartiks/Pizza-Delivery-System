from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings
from datetime import timedelta

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pizzeria.settings')
app = Celery('pizzeria')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'update-order-status-every-minute': {
        'task': 'your_app.tasks.update_order_status',
        'schedule': timedelta(minutes=1),  # Adjust the interval as needed
    },
}

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)