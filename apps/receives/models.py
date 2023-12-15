from django.db import models

# Create your models here.


class Receive(models.Model):
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    branch = models.ForeignKey('branches.Branch', on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    comment = models.TextField()
