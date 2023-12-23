from django.db import models

# Create your models here.


class Sale(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    datetime = models.IntegerField(default=0)
    price = models.FloatField(default=0)
    customer = models.ForeignKey(
        'customers.Customer', on_delete=models.CASCADE)
    branch = models.ForeignKey('branches.Branch', on_delete=models.CASCADE)
    comment = models.TextField(default="")
