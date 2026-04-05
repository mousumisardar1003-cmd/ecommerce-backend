from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ("username", "email", "phone", "is_staff", "is_seller", "is_active")
    list_filter = ("is_staff", "is_active", "is_seller")
    fieldsets = (
        (None, {"fields": ("username", "email", "phone", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "is_seller", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "email", "phone", "password1", "password2", "is_staff", "is_active", "is_seller")}
        ),
    )
    search_fields = ("email", "username", "phone")
    ordering = ("username",)


admin.site.register(CustomUser, CustomUserAdmin)
