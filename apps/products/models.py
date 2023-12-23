
from django.db import models
from django.utils.translation import gettext_lazy as _
# from apps.documents.models import BaseModel
# from apps.categories.models import Category
import uuid


def rename_image(instance, filename):
    new_image_name = uuid.uuid4()
    return f'images/products/{new_image_name}.{filename.split(".")[-1]}'


class Product(models.Model):
    name = models.CharField(_("Nomi"), max_length=255)
    category = models.ForeignKey(
        'categories.Category', on_delete=models.CASCADE, related_name="category_products")
    price = models.FloatField(_("Sotib olish narxi"), default=0)

    class Meta:
        verbose_name = _("Mahslulot")
        verbose_name_plural = _("Mahsulotlar")


class ProductImage(models.Model):
    product = models.ForeignKey(
        "products.product", on_delete=models.CASCADE, related_name='product_images')
    image = models.ImageField(upload_to=rename_image)
# Mahsulot klassi


# class SuiteItems(BaseModel):
#     suite = models.ForeignKey("product.product", on_delete=models.DO_NOTHING, verbose_name=_(
#         "Komplekt"), related_name="Suite")

#     class Meta:
#         verbose_name = _("Komplekt tarkibi")
#         db_table = 'set_connection'
# # komplekt


# class Stock(BaseModel):
#     branch = models.ForeignKey("branch.Branch", verbose_name=_(
#         "Filial"), on_delete=models.DO_NOTHING)

#     class Meta:
#         verbose_name = "Ombor"
#         verbose_name_plural = "Ombor"
#         db_table = 'stock'
# # ombor
