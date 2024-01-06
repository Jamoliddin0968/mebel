from django.db import models

# Create your models here.


class Notification(models.Model):
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)


class ScheduledNotification(models.Model):
    message = models.TextField()
    date = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=True)
