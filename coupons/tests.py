from django.test import TestCase
from django.utils import timezone
from .models import Coupon
from datetime import timedelta

class CouponTest(TestCase):
    def setUp(self):
        self.coupon = Coupon.objects.create(
            code="SAVE10",
            discount=10,
            active=True,
            valid_from=timezone.now() - timedelta(days=1),
            valid_to=timezone.now() + timedelta(days=1),
        )

    def test_coupon_is_valid(self):
        self.assertTrue(self.coupon.is_valid())

    def test_coupon_str(self):
        self.assertEqual(str(self.coupon), "SAVE10 - 10%")
