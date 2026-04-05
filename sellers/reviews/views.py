from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Review
from .forms import ReviewForm
from products.models import Product


@login_required
def add_review(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = request.user
            review.save()
            return redirect("products:product_detail", slug=product.slug)
    else:
        form = ReviewForm()

    return render(request, "add_review.html", {"form": form, "product": product})


def product_reviews(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    reviews = product.reviews.all()
    return render(request, "product_reviews.html", {"product": product, "reviews": reviews})
