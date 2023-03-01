from django.contrib import admin
from .models import UserSalary,CustomerManagement
# Register your models here.
@admin.register(UserSalary)
class UserSalaryAdmin(admin.ModelAdmin):
    list_display = ("user","cash","branch","date")
    list_display_links = ("user",)

