from django.test import TestCase
from django.contrib.auth.models import User
from products.models import Product
from .models import Order, OrderItem

class OrderTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="12345")
        self.product = Product.objects.create(name="Test Product", price=100)
        self.order = Order.objects.create(user=self.user, paid=False)
        self.item = OrderItem.objects.create(order=self.order, product=self.product, quantity=2, price=100)

    def test_order_total(self):
        self.assertEqual(self.order.get_total(), 200)

    def test_order_str(self):
        self.assertEqual(str(self.order), f"Order {self.order.id} by testuser")
