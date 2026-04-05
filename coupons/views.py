from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone
from .models import Coupon

def apply_coupon(request):
    if request.method == "POST":
        code = request.POST.get("code")
        try:
            coupon = Coupon.objects.get(code__iexact=code)
            if coupon.is_valid():
                request.session["coupon_id"] = coupon.id
                messages.success(request, f"Coupon {coupon.code} applied! {coupon.discount}% off.")
            else:
                messages.error(request, "This coupon is not valid or expired.")
        except Coupon.DoesNotExist:
            messages.error(request, "Invalid coupon code.")
        return redirect("cart:cart_detail")

    return render(request, "coupons/apply_coupon.html")
