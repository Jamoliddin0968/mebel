from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import (User,)
from django.contrib.auth.models import Group
admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    model = User
    list_display = ("username", "phone")
    list_display_links = ("username", "phone")
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
            "fields": ("phone", "first_name", "last_name", "patronymic",  "address"),
        }),
    )

    fieldsets = (
        ("Asosiy ma'lumotlar", {
            "fields": ("username",  "phone",  "first_name", "last_name", "patronymic", "address"),
        }),
    )
    # ordesring = ("id",)
# hodimlar

# ruhstanoma
