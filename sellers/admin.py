from django.contrib import admin
from .models import Seller

@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ("shop_name", "user", "phone", "verified", "created_at")
    list_filter = ("verified", "created_at")
    search_fields = ("shop_name", "user__username", "phone", "gst_number")
    ordering = ("-created_at",)
