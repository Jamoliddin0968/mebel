from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import (AllowedUsers, Customer, User,
                     Provider)
from django.contrib.auth.models import Group
admin.site.unregister(Group)
# hodimlar
@admin.register(User)
class UserAdmin(BaseUserAdmin):
    model = User
    list_display = ("username","name","phone")
    list_display_links = ("username","name","phone")
    # search_fields = ("username",)
    add_fieldsets = (
        (
            "Login , parol",
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2"),
            },
        ),
        ("", {
            "fields": ("name","phone","birth_date","percentage","branch"),
        }),
    )
    
    fieldsets = (
        ("Asosiy ma'lumotlar", {
            "fields": ("username","name","phone","birth_date","percentage","branch"),
        }),
    )
    # ordesring = ("id",)
# ruhstanoma
@admin.register(AllowedUsers)
class AllowedUsersAdmin(admin.ModelAdmin):
    list_display = ("user","branch")
    list_display_links = ("user","branch")

# Xaridor
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("name","phone","address")
    list_display_links = ("name",)
# Taminotchi
@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    list_display = ("name","phone","address")
    list_display_links = ("name",)


