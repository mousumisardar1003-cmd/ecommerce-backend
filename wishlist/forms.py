from django import forms
from .models import Wishlist
from products.models import Product


class WishlistAddForm(forms.Form):
    product_id = forms.IntegerField(widget=forms.HiddenInput)
