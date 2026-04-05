from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from products.models import Product, Category
from .models import Wishlist

User = get_user_model()


class WishlistTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="wishlistuser", password="testpass")
        self.client.force_authenticate(self.user)

        self.category = Category.objects.create(name="Electronics")
        self.product = Product.objects.create(
            name="Smartphone",
            description="Latest model",
            price=15000,
            stock=10,
            category=self.category
        )

    def test_add_to_wishlist(self):
        response = self.client.post("/api/wishlist/", {"product": self.product.id})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Wishlist.objects.filter(user=self.user).count(), 1)

    def test_get_wishlist(self):
        Wishlist.objects.create(user=self.user, product=self.product)
        response = self.client.get("/api/wishlist/")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.data) >= 1)
