
from django.db import models
from django.utils.translation import gettext_lazy as _

from documents.models import BaseModel


class Product(models.Model):
    name = models.CharField(_("Nomi"), max_length=255)
    material = models.CharField(_("Materiali"), max_length=255)
    size = models.CharField(_("O'lchami"), max_length=255)
    selling_price = models.PositiveIntegerField(_("Sotish narxi"))
    color = models.CharField(_("Rangi"), max_length=255)
    comment = models.CharField(_("Izoh"), max_length=255)
    price = models.PositiveIntegerField(_("Sotib olish narxi"), default=0)
    is_order = models.BooleanField(_("Buyurtma"), default=False)
    is_suite = models.BooleanField(_("Komplektmi"), default=False)

    class Meta:
        verbose_name = _("Mahslulot")
        verbose_name_plural = _("Mahsulotlar")
        db_table = 'product'
# Mahsulot klassi


class SuiteItems(BaseModel):
    suite = models.ForeignKey("product.product", on_delete=models.DO_NOTHING, verbose_name=_(
        "Komplekt"), related_name="Suite")

    class Meta:
        verbose_name = _("Komplekt tarkibi")
        db_table = 'set_connection'
# komplekt


class Stock(BaseModel):
    branch = models.ForeignKey("branch.Branch", verbose_name=_(
        "Filial"), on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = "Ombor"
        verbose_name_plural = "Ombor"
        db_table = 'stock'
# ombor
