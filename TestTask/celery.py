from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
import celery.signals

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TestTask.settings')

app = Celery('TestTask', include=['orders.tasks'])

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@celery.signals.beat_init.connect
def on_beat_init_disable_connection_pool(sender, **kwargs):
    sender.app.conf.BROKER_POOL_LIMIT = 0
