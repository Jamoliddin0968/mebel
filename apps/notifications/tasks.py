from __future__ import absolute_import, unicode_literals
from celery import shared_task
from apps.notifications.models import ScheduledNotification, Notification

from apps.users.models import User


@shared_task
def create_notifications(*args, **kwargs):
    users = User.objects.all()
    for notif in ScheduledNotification.objects.all():
        for user in users:
            Notification.objects.create(
                message=notif.message, user=user
            )
    return True
