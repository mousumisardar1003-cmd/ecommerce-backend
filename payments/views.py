import razorpay
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from orders.models import Order
from .models import Payment

client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

def checkout(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    amount = int(order.get_total() * 100)  # Razorpay needs paise

    razorpay_order = client.order.create(dict(amount=amount, currency="INR", payment_capture="1"))

    payment = Payment.objects.create(
        user=request.user,
        order=order,
        amount=order.get_total(),
        razorpay_order_id=razorpay_order["id"],   # ✅ Fixed
        status="PENDING",
    )

    context = {
        "order": order,
        "payment": payment,
        "razorpay_order_id": razorpay_order["id"],
        "razorpay_key_id": settings.RAZORPAY_KEY_ID,
        "amount": amount,
        "currency": "INR",
    }
    return render(request, "checkout.html", context)


@csrf_exempt
def verify_payment(request):
    if request.method == "POST":
        order_id = request.POST.get("razorpay_order_id")
        payment_id = request.POST.get("razorpay_payment_id")
        signature = request.POST.get("razorpay_signature")

        # ✅ Lookup by razorpay_order_id, not payment_id
        payment = get_object_or_404(Payment, razorpay_order_id=order_id)

        try:
            client.utility.verify_payment_signature({
                "razorpay_order_id": order_id,
                "razorpay_payment_id": payment_id,
                "razorpay_signature": signature
            })

            # ✅ Update payment record
            payment.status = "SUCCESS"
            payment.razorpay_payment_id = payment_id
            payment.razorpay_signature = signature
            payment.save()

            # ✅ Mark order as paid
            order = payment.order
            order.paid = True
            order.save()

            return render(request, "payment_success.html", {"order": order})

        except razorpay.errors.SignatureVerificationError:
            payment.status = "FAILED"
            payment.save()
            return render(request, "payment_failed.html", {"order": payment.order})

    return HttpResponse("Invalid request")
