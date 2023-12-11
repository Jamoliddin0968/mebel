from django.contrib import admin
from .models import Customer
# Register your models here.


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("first_name", "phone", "address")
    list_display_links = ("first_name",)
# Xaridor
