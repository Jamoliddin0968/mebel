from django.db import models
from django.utils.translation import gettext_lazy as _

OLINDI = "Olindi"
BERILDI = "Berildi"
OLINDI_KOEFFITSIYENT = -1
BERILDI_KOEFFITSIYENT = 1

MANAGE_TYPES = (
    (OLINDI_KOEFFITSIYENT, OLINDI),
    (BERILDI_KOEFFITSIYENT, BERILDI)
)

# haridor bilan hisob kitob


class CustomerManagement(models.Model):

    customer = models.ForeignKey(
        "users.Customer", models.DO_NOTHING, verbose_name=_("Haridor"))
    user = models.ForeignKey(
        'users.User', models.DO_NOTHING, verbose_name=_("Hodim"))
    cash = models.PositiveIntegerField(
        default=0, verbose_name=_("Pul miqdori"))
    status = models.IntegerField(choices=MANAGE_TYPES,verbose_name=_("Holati"))
    date = models.DateTimeField(auto_now_add=True)
    branch = models.ForeignKey("branch.Branch", verbose_name=_(
        "Filial"), on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.customer.name 
    
    class Meta:
        verbose_name = _("Xaridorlar bilan hisob-kitob")
        verbose_name_plural = _("Xaridorlar bilan hisob-kitob")
        db_table = 'customer_management'

class PayOffice(models.Model):
    user = models.ForeignKey(
        'users.User', models.DO_NOTHING, verbose_name=_("Hodim"))
    cash = models.IntegerField(default=0, verbose_name=_("Pul miqdori"))
    status = models.IntegerField(
        choices=MANAGE_TYPES, verbose_name=_("Holati"))
    date = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(verbose_name=_("Izoh"))
    branch = models.ForeignKey("branch.Branch", verbose_name=_(
        "Filial"), on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = _("Kassa")
        verbose_name_plural = _("Kassa kirim-chiqim")
        db_table = 'pay_office'

# Ishchilar maoshi


class UserSalary(models.Model):
    user = models.ForeignKey(
        "users.User", models.DO_NOTHING, verbose_name=_("Hodim"))
    cash = models.IntegerField(verbose_name=_("Pul miqdori"))
    date = models.DateTimeField(auto_now_add=True)
    branch = models.ForeignKey("branch.Branch", verbose_name=_(
        "Filial"), on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return self.user.name
    class Meta:
        verbose_name = _("Ishchilar maoshi")
        verbose_name_plural = _("Ishchilar maoshi")
        db_table = 'salary'
