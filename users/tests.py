from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


class UserTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser",
            email="test@example.com",
            password="testpass123",
            phone="9999999999"
        )

    def test_user_creation(self):
        self.assertEqual(self.user.username, "testuser")
        self.assertEqual(self.user.email, "test@example.com")
        self.assertFalse(self.user.is_seller)

    def test_login_view(self):
        login = self.client.login(username="testuser", password="testpass123")
        self.assertTrue(login)

    def test_register_view(self):
        response = self.client.get(reverse("users:register"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Register")
