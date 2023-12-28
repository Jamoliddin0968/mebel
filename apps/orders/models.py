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
