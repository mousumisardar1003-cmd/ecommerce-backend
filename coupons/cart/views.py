from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import CartItem
from products.models import Product

@login_required
def cart_detail(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total = sum(item.get_total_price() for item in cart_items)  # ✅ works now
    return render(request, "cart_detail.html", {"cart_items": cart_items, "total": total})

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect("cart:cart_detail")

@login_required
def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, user=request.user)
    item.delete()
    return redirect("cart:cart_detail")

@login_required
def update_quantity(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, user=request.user)
    if request.method == "POST":
        action = request.POST.get("action")
        if action == "increase":
            item.quantity += 1
            item.save()
        elif action == "decrease" and item.quantity > 1:
            item.quantity -= 1
            item.save()
    return redirect('cart:cart_detail')