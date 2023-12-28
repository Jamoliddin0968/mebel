from django.db import models

# Create your models here.


class Order(models.Model):
    customer = models.ForeignKey(
        'customers.Customer', on_delete=models.CASCADE)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    branch = models.ForeignKey('branches.Branch', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    view_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    price = models.DecimalField(max_digits=13, decimal_places=2)

    comment = models.TextField(default="")
    state = models.IntegerField(default=1)
    is_notificated = models.BooleanField(default=False)
    # notification


class OrderImages(models.Model):
    img = models.ImageField(upload_to='order/images')


class OrderItem(models.Model):
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    amount = models.FloatField(default=0)
    sizes = models.TextField()
    order = models.ForeignKey('orders.Order', on_delete=models.CASCADE)
