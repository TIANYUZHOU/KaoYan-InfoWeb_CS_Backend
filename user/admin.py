from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy

from .models import User


class MyUserAdmin(UserAdmin):
    list_display = ('id', 'username', 'mobile', 'email', 'date_joined', 'editTime')
    list_display_links = ('id', 'username')
    search_fields = ("username", "mobile", "email")
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (gettext_lazy("Personal info"),
         {"fields": ("email", "mobile", "avatar", "signature")}),
        (
            gettext_lazy("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (gettext_lazy("Important dates"), {"fields": ("last_login", "date_joined")}),
    )


# admin.site.unregister(User)
admin.site.register(User, MyUserAdmin)
