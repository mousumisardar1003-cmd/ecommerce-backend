from django import forms
from .models import Seller

class SellerForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = ["shop_name", "phone", "address", "gst_number"]
        widgets = {
            "shop_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Shop Name"}),
            "phone": forms.TextInput(attrs={"class": "form-control", "placeholder": "Phone Number"}),
            "address": forms.Textarea(attrs={"class": "form-control", "rows": 3, "placeholder": "Shop Address"}),
            "gst_number": forms.TextInput(attrs={"class": "form-control", "placeholder": "GST Number (optional)"}),
        }
