from django.db import models

from apps.notifications.models import ScheduledNotification


class ScheduledLoan(models.Model):
    customer = models.ForeignKey(
        'customers.Customer', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=11, decimal_places=2)
    date = models.DateField()
    is_notificated = models.BooleanField(default=False)
    notification = models.ForeignKey(
        ScheduledNotification, on_delete=models.CASCADE)
