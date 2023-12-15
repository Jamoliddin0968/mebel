from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.


class Customer(models.Model):
    first_name = models.CharField(_("Ism"), max_length=150, blank=True)
    last_name = models.CharField(_("Familiya"), max_length=150, blank=True)
    phone = models.CharField(max_length=255, verbose_name=_("Telefon raqam"))
    address = models.CharField(max_length=255, verbose_name=_("Manzil"))

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = _("Xaridor")
        verbose_name_plural = _("Xaridorlar")

    def get_full_name(self,):
        return f"{self.first_name} {self.last_name}"
