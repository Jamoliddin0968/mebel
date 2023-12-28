from django.db import models


class Loans(models.Model):
    customer = models.ForeignKey(
        'customers.Customer', on_delete=models.CASCADE)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    branch = models.ForeignKey('branches.Branch', on_delete=models.CASCADE)
    date = models.DateTimeField()
    price = models.DecimalField(max_digits=11, decimal_places=2)
