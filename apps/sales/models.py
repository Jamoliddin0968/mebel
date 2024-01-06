from django.db import models

# Create your models here.


class Sale(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=11, decimal_places=2)
    customer = models.ForeignKey(
        'customers.Customer', on_delete=models.CASCADE)
    branch = models.ForeignKey('branches.Branch', on_delete=models.CASCADE)
    comment = models.TextField(default="")


class SaleItem(models.Model):
    product = models.ForeignKey(
        "products.Product", on_delete=models.CASCADE)
    amount = models.FloatField(default=0)
    comment = models.TextField(default="")
    sale = models.ForeignKey(
        Sale, on_delete=models.CASCADE, related_name='sale_items')  # For
