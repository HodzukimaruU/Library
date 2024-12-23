from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'library_app.settings')

app = Celery('library_app')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_scheduler = 'django_celery_beat.schedulers:DatabaseScheduler'

app.autodiscover_tasks()
