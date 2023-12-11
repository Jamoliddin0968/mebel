from django.db import models


class WareHouse(models.Model):
    branch = models.ForeignKey('branches.Branch', on_delete=models.CASCADE)
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)
