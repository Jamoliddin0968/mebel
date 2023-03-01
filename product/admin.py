from django.contrib import admin

from product.models import (
    Order, OrderItem, Product, PrixodItems, Prixod
)
admin.site.register((Order, OrderItem, Product, PrixodItems, Prixod))
