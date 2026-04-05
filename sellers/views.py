from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Seller
from .forms import SellerForm

@login_required
def seller_dashboard(request):
    seller = getattr(request.user, "seller_profile", None)
    return render(request, "sellers/dashboard.html", {"seller": seller})

@login_required
def register_seller(request):
    if hasattr(request.user, "seller_profile"):
        return redirect("sellers:dashboard")

    if request.method == "POST":
        form = SellerForm(request.POST)
        if form.is_valid():
            seller = form.save(commit=False)
            seller.user = request.user
            seller.save()
            return redirect("sellers:dashboard")
    else:
        form = SellerForm()
    return render(request, "sellers/register.html", {"form": form})
