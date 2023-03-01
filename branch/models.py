from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.
#filial
class Branch(models.Model):
    name = models.CharField(_("nomi"), max_length=50)    
    adress = models.CharField(_("Manzili"), max_length=150)
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = _("Filial")
        verbose_name_plural = _("Filiallr")
        db_table = "branchs"
