from django.db import models

# Create your models here.


class Notification(models.Model):
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)


class ScheduledNotification(models.Model):
    message = models.TextField()
    date = models.DateField()
    status = models.BooleanField(default=True)


class ScheduledLoan(models.Model):
    customer = models.ForeignKey(
        'customers.Customer', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=11, decimal_places=2)
    date = models.DateField()
    is_notificated = models.BooleanField(default=False)
    notification = models.ForeignKey(
        ScheduledNotification, on_delete=models.CASCADE)
