from django.db import models


class WareHouse(models.Model):
    branch = models.ForeignKey('branches.Branch', on_delete=models.CASCADE)
