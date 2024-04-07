from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'facebook_clone.settings')

app = Celery('facebook_clone')
app.config_from_object('django.conf:settings', namespace='CELERY', )
app.conf.timezone = 'America/Sao_Paulo'

app.autodiscover_tasks()
