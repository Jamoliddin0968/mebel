from django.db import models

from apps.notifications.models import ScheduledNotification


class ScheduledLoan(models.Model):
    customer = models.ForeignKey(
        'customers.Customer', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=11, decimal_places=2)
    receive_date = models.DateField(null=True, blank=True)
    is_notificated = models.BooleanField(default=False)
    date = models.DateField(null=True, blank=True)
    notification = models.ForeignKey(
        ScheduledNotification, on_delete=models.CASCADE)
