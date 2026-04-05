from django.db import models
from django.conf import settings
from products.models import Product  # adjust if your product model is elsewhere

class CartItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.user} - {self.product} (x{self.quantity})"

    # ✅ Add this method
    def get_total_price(self):
        return self.product.price * self.quantity
