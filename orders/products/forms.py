from django import forms
from .models import Product, Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name", "slug"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Category Name"}),
            "slug": forms.TextInput(attrs={"class": "form-control", "placeholder": "Slug (auto or custom)"}),
        }


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["category", "name", "slug", "description", "price", "stock", "available", "image"]
        widgets = {
            "category": forms.Select(attrs={"class": "form-select"}),
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Product Name"}),
            "slug": forms.TextInput(attrs={"class": "form-control", "placeholder": "Slug (auto or custom)"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 4, "placeholder": "Product Description"}),
            "price": forms.NumberInput(attrs={"class": "form-control", "placeholder": "Price in ₹"}),
            "stock": forms.NumberInput(attrs={"class": "form-control", "placeholder": "Available Stock"}),
            "available": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "image": forms.FileInput(attrs={"class": "form-control"}),
        }
