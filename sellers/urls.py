from django.urls import path
from . import views

app_name = "sellers"

urlpatterns = [
    path("dashboard/", views.seller_dashboard, name="dashboard"),
    path("register/", views.register_seller, name="register"),
]
