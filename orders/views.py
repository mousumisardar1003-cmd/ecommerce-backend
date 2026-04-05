from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from cart.models import CartItem
from .models import Order, OrderItem

# Checkout view (was create_order)
@login_required
def checkout(request):
    cart_items = CartItem.objects.filter(user=request.user)
    if not cart_items.exists():
        return redirect("cart:cart_detail")

    # Create a new order
    order = Order.objects.create(user=request.user, paid=False)

    # Create order items from cart items
    for item in cart_items:
        OrderItem.objects.create(
            order=order,
            product=item.product,
            quantity=item.quantity,
            price=item.product.price,
        )

    # Clear the cart after creating order items
    cart_items.delete()

    # Redirect to order detail page
    return redirect("orders:order_detail", order_id=order.id)


# View to list user's orders
@login_required
def my_orders(request):
    orders = Order.objects.filter(user=request.user).order_by("-created_at")
    return render(request, "orders/my_orders.html", {"orders": orders})


# View for order details
@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, "order_detail.html", {"order": order})
