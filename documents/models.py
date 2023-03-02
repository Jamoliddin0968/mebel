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
    # total_sum = models.IntegerField(_("Summa"),default=0)
    date = models.DateTimeField(auto_now_add=True)
    branch = models.ForeignKey("branch.Branch", verbose_name=_(
        "Filial"), on_delete=models.DO_NOTHING)

    class Meta:
        abstract = True
# document base


class BaseModel(models.Model):
    product = models.ForeignKey(
        "product.Product", models.DO_NOTHING, verbose_name=_("Mahsulot"))
    quantity = models.IntegerField(verbose_name=_("Miqdori"))
    price = models.PositiveIntegerField(default=0, verbose_name=_("Narxi"))

    def __str__(self):
        return self.product.name

    class Meta:
        abstract = True
# hujjat tarkibi uchun


"""                              Xaridorlar bilan hisob kitoblar                               """


class CustomerManagement(DocumentBaseModel):
    customer = models.ForeignKey(
        "users.Customer", models.DO_NOTHING, verbose_name=_("Haridor"))
    cash = models.PositiveIntegerField(
        default=0, verbose_name=_("Pul miqdori"))
    status = models.IntegerField(
        choices=MANAGE_TYPES, verbose_name=_("Holati"))

    def __str__(self):
        return self.customer.name

    class Meta:
        verbose_name = _("Xaridorlar bilan hisob-kitob")
        verbose_name_plural = _("Xaridorlar bilan hisob-kitob")
        db_table = 'customer_management'
# haridor bilan hisob kitob


class CustomerSendBack(DocumentBaseModel):
    customer = models.ForeignKey(
        "users.Customer", models.DO_NOTHING, verbose_name="Haridor")
    total_sum = models.IntegerField(_("Summa"))

    class Meta:
        verbose_name = "Xaridorga vozvrat"
        verbose_name_plural = "Xaridorga vozvrat"
        db_table = 'take_back'
# Xaridorga tovar qaytarish


class CustomerSendBackItems(BaseModel):
    CustomerSendBack = models.ForeignKey("documents.CustomerSendBack", verbose_name=_(
        "tovar vozvrat"), on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = "Xaridorga vozvrat hujjati tarkibi"
        verbose_name_plural = "Xaridorga vozvrat hujjati tarkibi"
        db_table = 'taken_back'
# Xaridorga tovar qaytarish tarkibi


"""                                      Kassa hujjati                                          """


class PayOffice(DocumentBaseModel):
    cash = models.IntegerField(default=0, verbose_name=_("Pul miqdori"))
    status = models.IntegerField(
        choices=MANAGE_TYPES, verbose_name=_("Holati"))
    comment = models.TextField(verbose_name=_("Izoh"))

    class Meta:
        verbose_name = _("Kassa")
        verbose_name_plural = _("Kassa kirim-chiqim")
        db_table = 'pay_office'
# kassa hujjati


class Orders(DocumentBaseModel):

    customer = models.ForeignKey(
        "users.Customer", models.DO_NOTHING, verbose_name=_("Xaridor"))
    cost = models.IntegerField(_("Narxi"))
    total_sum = models.IntegerField(_("Summa"), default=0)

    def __str__(self):
        return self.customer

    class Meta:
        verbose_name = _("Buyurtma")
        verbose_name_plural = _("Buyurtmalar")
        db_table = 'orders'
# Buyurtmalar hujjati


class OrderItem(BaseModel):
    order = models.ForeignKey(Orders, verbose_name=_(
        "Buyurtma"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Buyutma tarkibi")
        verbose_name_plural = _("Buyutmalar tarkibi")
        db_table = 'order_items'
# Buyurtma hujjati tarkibi


class Prixod(DocumentBaseModel):

    provider = models.ForeignKey("users.Provider", models.DO_NOTHING)
    total_sum = models.IntegerField(_("Summa"))

    def __str__(self) -> str:
        return self.provider.name

    class Meta:
        verbose_name = _("Prixod hujjati")
        verbose_name_plural = _("Prixodlar")
        db_table = 'receive'
# Prixod hujjati


class PrixodItems(BaseModel):
    prixod = models.ForeignKey("documents.Prixod", verbose_name=_(
        "Prixod"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Prixod tarkibi")
        verbose_name_plural = _("Prixodlar tarkibi")
        db_table = 'receive_items'
# Prixod hujjati uchun Pricod tarkibi


class Sell(DocumentBaseModel):
    customer = models.ForeignKey(
        "users.Customer", verbose_name=_("Xaridor"), on_delete=models.DO_NOTHING)
    total_sum = models.IntegerField(_("Summa"))

    def __str__(self) -> str:
        return self.customer.name

    class Meta:
        verbose_name = _("Sotuvlar")
        verbose_name_plural = _("Sotuvlar")
        db_table = 'sell'
# Sotuvlar sotub hujjati uchun


class SellItem(BaseModel):
    sell = models.ForeignKey("documents.Sell", verbose_name=_(
        "Sotuv hujjati"), on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = _("Sotuv tarkibi")
        verbose_name_plural = _("Sotuv tarkibi")
        db_table = 'sell_item'
# sotuv hujjati tarkibi


"""                              Xaridorlar bilan hisob kitoblar                               """


class ProviderSendBack(DocumentBaseModel):
    provider = models.ForeignKey(
        "users.Provider", models.DO_NOTHING, verbose_name="Ta'minotchi")

    class Meta:
        verbose_name = "Ta'minotchiga mahsulot qaytarish"
        verbose_name_plural = "Ta'minotchiga mahsulot qaytarish"
        db_table = 'send_back'
# ta'minotchiga qaytarish


class ProviderSendBackItems(BaseModel):
    provider_send_back = models.ForeignKey("documents.ProviderSendBack", verbose_name=_(
        "tovar vozvrat"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Taminotchiga vozvrat hujjati tarkibi")
        verbose_name_plural = _("Taminotchiga vozvrat hujjati tarkibi")
        db_table = 'sent_back'
# ta'minotchiga qaytarish hujjati tarkibi


class ProviderManagement(DocumentBaseModel):
    provider = models.ForeignKey(
        "users.Provider", models.DO_NOTHING, verbose_name=_("Ta'minotchi"))
    cash = models.IntegerField(verbose_name=_("Pul miqdori"))
    status = models.IntegerField(
        choices=MANAGE_TYPES, verbose_name=_("Holati"))

    def __str__(self) -> str:
        return self.provider.name

    class Meta:
        verbose_name = _("Ta'minotchi bilan hiosb-kitob")
        verbose_name_plural = _("Ta'minotchi bilan hiosb-kitob")
        db_table = 'provider_management'
# Ta'minotchi bilan hiosb-kitob


"""                                     spisaniya                                            """


class WriteOff(DocumentBaseModel):
    comment = models.CharField(max_length=255)

    class Meta:
        verbose_name = _("Spisaniya")
        verbose_name_plural = _("Spisaniya")
        db_table = 'write_off'
# spisaniya hujjati


class WriteOffItems(BaseModel):
    write_off = models.ForeignKey("documents.WriteOff", verbose_name=_(
        "Spisaniya"), on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = _("Spisaniya hujjati tarkibi")
        verbose_name_plural = _("Spisaniya hujjati tarkibi")
        db_table = 'written_off'
# spisaniya hujjati takibi


"""                              hodimlar bilan hisob kitoblar                               """


class Penalty(DocumentBaseModel):
    cash = models.IntegerField(default=0, verbose_name=_("Pul miqdori"))

    class Meta:
        verbose_name = _("Jarima")
        verbose_name_plural = _("Jarimalar")
        db_table = 'penalty'
# Jarimalar


class Timtable(DocumentBaseModel):
    user = models.ForeignKey("users.User", models.DO_NOTHING,)
    user = None
    class Meta:
        verbose_name = _("davomat hujjati")
        verbose_name_plural = _("davomat hujjati")
        db_table = 'timtable'
# davomat hujjati

class TimtableItems(models.Model):
    come = models.TimeField(verbose_name=_("Kelgan vaqti"))
    go_back = models.TimeField(_("Ketgan vaqti"))
    class Meta:
        verbose_name = _("davomat hujjati tarkibi")
        verbose_name_plural = _("davomat hujjati tarkibi")
        db_table = 'timtable_items'
# davomat hujjati tarkibi

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
# Ishchilar maoshi
