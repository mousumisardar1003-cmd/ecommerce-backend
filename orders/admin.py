from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'status', 'get_total']
    list_filter = ['status']
    inlines = [OrderItemInline]

    def get_total(self, obj):
        return sum(item.product.price * item.quantity for item in obj.items.all())
    get_total.short_description = "Total Amount"
