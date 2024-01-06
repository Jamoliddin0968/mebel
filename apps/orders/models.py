from django.db import models

from apps.notifications.models import ScheduledNotification

EMPTY = 0
COMPLETED = 1
NOT_INSTALLED = 2
NOT_FILLED = 3
IN_PROGRESS = 4
STATES = ((EMPTY, EMPTY), (COMPLETED, COMPLETED), (NOT_INSTALLED, NOT_INSTALLED),
          (NOT_FILLED, NOT_FILLED), (IN_PROGRESS, IN_PROGRESS))


class Order(models.Model):
    # required
    customer = models.ForeignKey(
        'customers.Customer', on_delete=models.CASCADE)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    branch = models.ForeignKey('branches.Branch', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    view_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    completion_date = models.DateField(null=True, blank=True)
    price = models.DecimalField(max_digits=13, decimal_places=2, default=0)

    comment = models.TextField(default="")
    state = models.IntegerField(choices=STATES, default=EMPTY)
    is_notificated = models.BooleanField(default=False)
    notification = models.ForeignKey(
        ScheduledNotification, on_delete=models.SET_NULL, null=True, blank=True)


class OrderImage(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name="order_images")
    img = models.ImageField(upload_to='order/images')


class OrderItem(models.Model):
    order = models.ForeignKey('orders.Order', on_delete=models.CASCADE)
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    amount = models.FloatField(default=0)
    sizes = models.TextField()
