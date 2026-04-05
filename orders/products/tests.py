from django.test import TestCase
from .models import Category, Product

class ProductTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Clothing", slug="clothing")
        self.product = Product.objects.create(
            category=self.category,
            name="T-Shirt",
            slug="t-shirt",
            description="A cool cotton t-shirt",
            price=499,
            stock=10,
            available=True,
        )

    def test_product_str(self):
        self.assertEqual(str(self.product), "T-Shirt")

    def test_category_str(self):
        self.assertEqual(str(self.category), "Clothing")
