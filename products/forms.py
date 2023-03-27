from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title','description','featured_image','category','price','tags']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Product title', 'class': 'prodinput'}),
            'description': forms.Textarea(
                attrs={'placeholder': 'Enter description here'}),
        }