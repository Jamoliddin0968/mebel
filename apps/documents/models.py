from django.db import models
from django.utils.translation import gettext_lazy as _

KIRIM = "Kirim"
CHIQIM = "Chiqim"
KIRIM_KOEFFITSIYENT = 1
CHIQIM_KOEFFITSIYENT = -1

MANAGE_TYPES = (
    (KIRIM_KOEFFITSIYENT, KIRIM),
    (CHIQIM_KOEFFITSIYENT, CHIQIM)
)


"""                                      Base modellar                                 """


class DocumentBaseModel(models.Model):
    user = models.ForeignKey(
        'users.User', models.DO_NOTHING, verbose_name=_("Hodim"))
    total_sum = models.IntegerField(_("Summa"),default=0)
    date = models.DateTimeField(verbose_name=_("Vaqti"))
    comment = models.TextField(_("verbose_name"),default="",null=True,blank=True)
    branch = models.ForeignKey("branch.Branch", verbose_name=_(
        "Filial"), on_delete=models.DO_NOTHING)

    class Meta:
        abstract = True
# document base


class BaseModel(models.Model):
    product = models.ForeignKey(
        "products.Product", models.DO_NOTHING, verbose_name=_("Mahsulot"))
    quantity = models.IntegerField(verbose_name=_("Miqdori"))

    def __str__(self):
        return self.product.name

    class Meta:
        abstract = True
# hujjat tarkibi uchun


"""                              Xaridorlar bilan hisob kitoblar                               """


class CustomerManagement(DocumentBaseModel):
    customer = models.ForeignKey(
        "users.Customer", models.DO_NOTHING, verbose_name=_("Haridor"))
    order = models.ForeignKey("documents.Orders", verbose_name=_("buyurtma"), on_delete=models.DO_NOTHING,null=True,blank=True)

    def __str__(self):
        return self.customer.name

    class Meta:
        verbose_name = _("Xaridorlar bilan hisob-kitob")
        verbose_name_plural = _("Xaridorlar bilan hisob-kitob")
# haridor bilan hisob kitob


class CustomerSendBack(DocumentBaseModel):
    customer = models.ForeignKey(
        "users.Customer", models.DO_NOTHING, verbose_name="Haridor")

    class Meta:
        verbose_name = "Xaridorga vozvrat"
        verbose_name_plural = "Xaridorga vozvrat"
# Xaridorga tovar qaytarish


class CustomerSendBackItems(BaseModel):
    CustomerSendBack = models.ForeignKey("documents.CustomerSendBack", verbose_name=_(
        "tovar vozvrat"), on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = "Xaridorga vozvrat hujjati tarkibi"
        verbose_name_plural = "Xaridorga vozvrat hujjati tarkibi"
# Xaridorga tovar qaytarish tarkibi


"""                                      Kassa hujjati                                          """

class PayOffice(DocumentBaseModel):
    class Meta:
        verbose_name = _("Kassa")
        verbose_name_plural = _("Kassa kirim-chiqim")
# kassa hujjati

class Prixod(DocumentBaseModel):
    provider = models.ForeignKey("users.Provider", models.DO_NOTHING)

    def __str__(self) -> str:
        return self.provider.name

    class Meta:
        verbose_name = _("Prixod hujjati")
        verbose_name_plural = _("Prixodlar")
# Prixod hujjati


class PrixodItems(BaseModel):
    prixod = models.ForeignKey("documents.Prixod", verbose_name=_(
        "Prixod"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Prixod tarkibi")
        verbose_name_plural = _("Prixodlar tarkibi")
# Prixod hujjati uchun Pricod tarkibi


class Sell(DocumentBaseModel):
    customer = models.ForeignKey(
        "users.Customer", verbose_name=_("Xaridor"), on_delete=models.DO_NOTHING)
    discount = models.PositiveIntegerField(_("chegirma"))

    def __str__(self) -> str:
        return self.customer.name

    class Meta:
        verbose_name = _("Sotuvlar")
        verbose_name_plural = _("Sotuvlar")
# Sotuvlar sotub hujjati uchun


class SellItem(BaseModel):
    sell = models.ForeignKey("documents.Sell", verbose_name=_(
        "Sotuv hujjati"), on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = _("Sotuv tarkibi")
        verbose_name_plural = _("Sotuv tarkibi")
# sotuv hujjati tarkibi


"""                                   Buyurtmalar hujjati                                        """

class Orders(DocumentBaseModel):
    customer = models.ForeignKey(
        "users.Customer", models.DO_NOTHING, verbose_name=_("Xaridor"))
    def __str__(self):
        return self.customer

    class Meta:
        verbose_name = _("Buyurtma")
        verbose_name_plural = _("Buyurtmalar")
# Buyurtmalar hujjati


class OrderItem(BaseModel):
    order = models.ForeignKey(Orders, verbose_name=_(
        "Buyurtma"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Buyutma tarkibi")
        verbose_name_plural = _("Buyutmalar tarkibi")
# Buyurtma hujjati tarkibi


"""                              Xaridorlar bilan hisob kitoblar                               """


class ProviderSendBack(DocumentBaseModel):
    provider = models.ForeignKey(
        "users.Provider", models.DO_NOTHING, verbose_name="Ta'minotchi")

    class Meta:
        verbose_name = "Ta'minotchiga mahsulot qaytarish"
        verbose_name_plural = "Ta'minotchiga mahsulot qaytarish"
# ta'minotchiga qaytarish


class ProviderSendBackItems(BaseModel):
    provider_send_back = models.ForeignKey("documents.ProviderSendBack", verbose_name=_(
        "tovar vozvrat"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Taminotchiga vozvrat hujjati tarkibi")
        verbose_name_plural = _("Taminotchiga vozvrat hujjati tarkibi")
# ta'minotchiga qaytarish hujjati tarkibi


class ProviderManagement(DocumentBaseModel):
    provider = models.ForeignKey(
        "users.Provider", models.DO_NOTHING, verbose_name=_("Ta'minotchi"))
    cash = models.IntegerField(verbose_name=_("Pul miqdori"))
    prixod = models.ForeignKey("documents.Prixod", verbose_name=_(""), on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.provider.name

    class Meta:
        verbose_name = _("Ta'minotchi bilan hiosb-kitob")
        verbose_name_plural = _("Ta'minotchi bilan hiosb-kitob")
# Ta'minotchi bilan hiosb-kitob


"""                                     spisaniya                                            """


class WriteOff(DocumentBaseModel):
    comment = models.CharField(max_length=255)

    class Meta:
        verbose_name = _("Spisaniya")
        verbose_name_plural = _("Spisaniya")
# spisaniya hujjati


class WriteOffItems(BaseModel):
    write_off = models.ForeignKey("documents.WriteOff", verbose_name=_(
        "Spisaniya"), on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = _("Spisaniya hujjati tarkibi")
        verbose_name_plural = _("Spisaniya hujjati tarkibi")
# spisaniya hujjati takibi


"""                              hodimlar bilan hisob kitoblar                               """


class Penalty(DocumentBaseModel):
    
    class Meta:
        verbose_name = _("Jarima")
        verbose_name_plural = _("Jarimalar")
# Jarimalar


class Timtable(DocumentBaseModel):
    user = models.ForeignKey("users.User", models.DO_NOTHING)
    date = models.DateField(_("Sana"))
    class Meta:
        verbose_name = _("davomat hujjati")
        verbose_name_plural = _("davomat hujjati")
# davomat hujjati

class TimtableItems(models.Model):
    tim_table = models.ForeignKey(Timtable, verbose_name=_("Davomat hujjati"), on_delete=models.CASCADE)
    worker = models.ForeignKey("users.User", models.DO_NOTHING)
    come = models.TimeField(verbose_name=_("Kelgan vaqti"))
    go_back = models.TimeField(_("Ketgan vaqti"))
    comment = models.TextField()
    class Meta:
        verbose_name = _("davomat hujjati tarkibi")
        verbose_name_plural = _("davomat hujjati tarkibi")
# davomat hujjati tarkibi

class UserSalary(models.Model):
    user = models.ForeignKey(
        "users.User", models.DO_NOTHING, verbose_name=_("Hodim"))
    cash = models.IntegerField(verbose_name=_("Pul miqdori"))
    date = models.DateTimeField()
    branch = models.ForeignKey("branch.Branch", verbose_name=_(
        "Filial"), on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return self.user.name

    class Meta:
        verbose_name = _("Ishchilar maoshi")
        verbose_name_plural = _("Ishchilar maoshi")
# Ishchilar maoshi
