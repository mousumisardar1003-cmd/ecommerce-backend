from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from reviews.models import Review


def search_products(request):
    query = request.GET.get('q', '')
    sort = request.GET.get('sort', '')

    # Base search query
    products = Product.objects.filter(name__icontains=query) | Product.objects.filter(category__name__icontains=query)

    # ✅ Sorting logic
    if sort == "price_low_high":
        products = products.order_by("price")
    elif sort == "price_high_low":
        products = products.order_by("-price")
    elif sort == "newest":
        products = products.order_by("-created_at")
    elif sort == "name":
        products = products.order_by("name")

    return render(request, 'products/search_results.html', {
        'products': products,
        'query': query,
        'sort': sort
    })

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)


    # ✅ Filter by category (if URL contains category slug)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    # ✅ Filtering (price range, keyword search)
    min_price = request.GET.get("min_price")
    max_price = request.GET.get("max_price")
    q = request.GET.get("q")  # keyword search

    if min_price:
        products = products.filter(price__gte=min_price)
    if max_price:
        products = products.filter(price__lte=max_price)
    if q:
        products = products.filter(name__icontains=q)

    # ✅ Sorting
    sort = request.GET.get("sort")
    if sort == "price_low_high":
        products = products.order_by("price")
    elif sort == "price_high_low":
        products = products.order_by("-price")
    elif sort == "newest":
        products = products.order_by("-created_at")
    elif sort == "name":
        products = products.order_by("name")

    # ✅ Now return only after filters & sorting applied
    return render(request, "product_list.html", {
        "category": category,
        "categories": categories,
        "products": products
    })


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, available=True)

    # Fetch similar products based on same category (exclude current one)
    similar_products = Product.objects.filter(
        category=product.category,
        available=True
    ).exclude(id=product.id)[:4]  # show only 4

    # Reviews (if you already have this)
    reviews = Review.objects.filter(product=product).order_by("-created_at")

    return render(request, "product_detail.html", {
        "product": product,
        "reviews": reviews,
        "similar_products": similar_products
    })


