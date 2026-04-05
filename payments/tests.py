from django.test import TestCase
from django.contrib.auth.models import User
from orders.models import Order
from .models import Payment

class PaymentTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="12345")
        self.order = Order.objects.create(user=self.user, paid=False)
        self.payment = Payment.objects.create(user=self.user, order=self.order, amount=500)

    def test_payment_str(self):
        self.assertEqual(str(self.payment), f"Payment {self.payment.id} - testuser (PENDING)")
