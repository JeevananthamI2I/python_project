from django import forms
from .models import Product
from .models import Category

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'product_category', 'feature', 'price']
        
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']