from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings
from datetime import timedelta
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pizzeria.settings")
app = Celery('pizzeria')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks() #lambda: settings.INSTALLED_APPS

@app.task(bind=True)
def debug_task(self):
    """A debug celery task"""
    print(f"Request: {self.request!r}")
