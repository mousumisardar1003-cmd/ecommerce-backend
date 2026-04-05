from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView  # for homepage

urlpatterns = [
    path("admin/", admin.site.urls),

    # Homepage
    path("", TemplateView.as_view(template_name="home.html"), name="home"),

    # Authentication
    path("login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="home"), name="logout"),

    # Apps
    path("products/", include("products.urls")),
    path("cart/", include("cart.urls")),
    path("orders/", include("orders.urls")),
    path("users/", include("users.urls")),
    path("sellers/", include("sellers.urls")),
    path("payments/", include("payments.urls")),
    path("reviews/", include("reviews.urls")),
    path("coupons/", include("coupons.urls")),
    path("wishlist/", include("wishlist.urls")),
    path("products/", include("products.urls")),
]

# MEDIA & STATIC FILES (Dev only)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
