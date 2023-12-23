from django.db import models

# Create your models here.


class Receive(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    branch = models.ForeignKey('branches.Branch', on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)
    comment = models.TextField()


class ReceiveItem(models.Model):
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    amount = models.FloatField(default=0)
    receive = models.ForeignKey(Receive, on_delete=models.CASCADE)
