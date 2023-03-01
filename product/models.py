
from django.db import models
from django.utils.translation import gettext_lazy as _
# Mahsulot klassi
class Product(models.Model):
    name = models.CharField(_("Nomi"),max_length=255)
    material = models.CharField(_("Materiali"),max_length=255)
    size = models.CharField(_("O'lchami"),max_length=255)
    selling_price = models.PositiveIntegerField(_("Sotish narxi"))
    color = models.CharField(_("Rangi"),max_length=255)
    comment = models.CharField(_("Izoh"),max_length=255)
    price = models.PositiveIntegerField(_("Sotib olish narxi"),default=0)
    is_order = models.BooleanField(_("Buyurtma"),default=False)  
    is_set = models.BooleanField(_("Komplektmi"),default=False)  
    
    class Meta:
        verbose_name = _("Mahslulot")
        verbose_name_plural = _("Mahsulotlar")
        db_table = 'product'

# Buyurtmalar
class Order(models.Model):
    user = models.ForeignKey("users.User", models.DO_NOTHING,verbose_name=_("Hodim"))
    customer = models.ForeignKey("users.Customer", models.DO_NOTHING,verbose_name=_("Xaridor"))
    cost = models.IntegerField(_("Narxi"))
    total_sum = models.IntegerField(_("Summa"),default=0)
    date = models.DateField(auto_now_add=True,verbose_name=_("Vaqt"))
    branch = models.ForeignKey("branch.Branch", verbose_name=_("Filial"), on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return self.customer
    class Meta:
        verbose_name = _("Buyurtma")
        verbose_name_plural = _("Buyurtmalar")
        db_table = 'orders'
        
# Buyurtma tarkibi
class OrderItem(models.Model):
    order = models.ForeignKey(Order,verbose_name=_("Buyurtma"), on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING,verbose_name=_("Tovar")) 
    quantity = models.IntegerField(_("Miqdori"))

    class Meta:
        verbose_name = _("Buyutma tarkibi")
        verbose_name_plural = _("Buyutmalar tarkibi")
        db_table = 'order_items'

# Prixod       
class Prixod(models.Model):
    user = models.ForeignKey('users.User', models.DO_NOTHING)
    provider = models.ForeignKey("users.Provider", models.DO_NOTHING)
    total_sum = models.IntegerField(_("Summa"))
    date = models.DateTimeField()
    branch = models.ForeignKey("branch.Branch", verbose_name=_("Filial"), on_delete=models.DO_NOTHING)
    def __str__(self) -> str:
        return self.provider.name
    class Meta:
        verbose_name = _("Kirim hujjati")
        verbose_name_plural = _("Kirimlar")
        db_table = 'receive'

# Prixod hujjati uchun Pricod tarkibi       
class PrixodItems(models.Model):
    prixod = models.ForeignKey("product.Prixod", verbose_name=_("Prixod"), on_delete=models.CASCADE)
    product = models.IntegerField()
    quantity = models.IntegerField()

    class Meta:
        verbose_name = _("Prixod tarkibi")
        verbose_name_plural = _("Prixodlar tarkibi")
        db_table = 'receive_items'

# Sotuvlar sotub hujjati uchun
class Sell(models.Model):
    user = models.ForeignKey("users.User",verbose_name=_("Xodim"), on_delete=models.DO_NOTHING)
    customer = models.ForeignKey(
        "users.Customer",verbose_name=_("Xaridor"),on_delete=models.DO_NOTHING)
    total_sum = models.IntegerField(_("Summa"))
    date = models.DateTimeField(auto_now_add=True)
    branch = models.ForeignKey("branch.Branch", verbose_name=_("Filial"), on_delete=models.DO_NOTHING)
    
    def __str__(self) -> str:
        return self.customer.name
    
    class Meta:
        verbose_name = _("Sotuvlar")
        verbose_name_plural = _("Sotuvlar")
        db_table = 'sell'
# sotuv hujjati tarkibi
class SellItem(models.Model):
    sell = models.ForeignKey("product.Sell", verbose_name=_("Sotuv hujjati"), on_delete=models.DO_NOTHING)
    product = models.ForeignKey( Product, models.DO_NOTHING, verbose_name=_("Mahsulot"))
    quantity = models.IntegerField(verbose_name=_("Miqdori"))

    class Meta:
        verbose_name = _("Sotuv tarkibi")
        verbose_name = _("Sotuv tarkibi")
        db_table = 'sell_item'

# class SendBack(models.Model):
#     user = models.ForeignKey("users.User", models.DO_NOTHING)
#     provider = models.ForeignKey(
#         "users.Provider", models.DO_NOTHING)
#     date = models.DateTimeField()

#     class Meta:
#         db_table = 'send_back'

# class SentBack(models.Model):
#     product = models.ForeignKey(Product, models.DO_NOTHING)
#     quantity = models.IntegerField()

#     class Meta:

#         db_table = 'sent_back'

# class SetConnection(models.Model):

#     product = models.ForeignKey(
#         Product, models.DO_NOTHING)
#     quantity = models.IntegerField()

#     class Meta:

#         db_table = 'set_connection'

# class Stock(models.Model):

#     product = models.ForeignKey(
#         Product, models.DO_NOTHING, blank=True, null=True)
#     quantity = models.IntegerField(blank=True, null=True)

#     class Meta:

#         db_table = 'stock'

# class TakeBack(models.Model):
#     user = models.ForeignKey("users.User", models.DO_NOTHING)
#     customer = models.ForeignKey(
#         "users.Customer", models.DO_NOTHING)
#     date = models.IntegerField()

#     class Meta:

#         db_table = 'take_back'

# class TakenBack(models.Model):

#     product = models.ForeignKey(
#         Product, models.DO_NOTHING)
#     quantity = models.IntegerField()

#     class Meta:

#         db_table = 'taken_back'

# class Timtable(models.Model):
#     user = models.ForeignKey("users.User", models.DO_NOTHING)
#     come = models.DateTimeField()
#     go_back = models.DateTimeField()

#     class Meta:

#         db_table = 'timtable'

# class WriteOff(models.Model):
#     user = models.ForeignKey("users.User", models.DO_NOTHING)
#     comment = models.CharField(max_length=255)
#     date = models.DateTimeField()

#     class Meta:

#         db_table = 'write_off'

# class WrittenOff(models.Model):
#     product = models.ForeignKey(
#         Product, models.DO_NOTHING)
#     quantity = models.IntegerField()

#     class Meta:

#         db_table = 'written_off'
