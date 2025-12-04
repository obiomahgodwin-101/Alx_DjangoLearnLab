from django.contrib import admin
from .models import Book, CustomUser
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ("username", "email", "date_of_birth", "is_staff", "is_active")
    fieldsets = UserAdmin.fieldsets + (
        (
            "Additional Info",
            {"fields": ("date_of_birth", "profile_photo")},
        ),
    )


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Book)

