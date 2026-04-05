from django.test import TestCase
from django.contrib.auth.models import User
from products.models import Product
from .models import CartItem

class CartItemTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="12345")
        self.product = Product.objects.create(name="Test Product", price=100)
        self.cart_item = CartItem.objects.create(user=self.user, product=self.product, quantity=2)

    def test_cart_item_total_price(self):
        self.assertEqual(self.cart_item.get_total_price(), 200)

    def test_cart_item_str(self):
        self.assertEqual(str(self.cart_item), "Test Product (2)")
