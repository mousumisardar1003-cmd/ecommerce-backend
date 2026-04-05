from django.contrib import admin
from .models import CartItem

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product', 'quantity', 'get_total_price']

    def get_total_price(self, obj):
        return obj.product.price * obj.quantity
    get_total_price.short_description = "Total Price"
