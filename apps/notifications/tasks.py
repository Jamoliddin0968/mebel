from __future__ import absolute_import, unicode_literals
from celery import shared_task
from apps.notifications.models import ScheduledNotification, Notification


@shared_task
def create_notifications(*args, **kwargs):
    for notif in ScheduledNotification.objects.all():
        # Notification.objects.create()
        pass
    return True
