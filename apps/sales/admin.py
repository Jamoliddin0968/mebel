from django.contrib import admin

from .models import Sale,SaleItem

admin.site.register([Sale,SaleItem])
