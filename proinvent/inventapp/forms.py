from django import forms
from .models import Items

class ItemForm(forms.ModelForm):
    class Meta:
        model = Items
        fields = ['product_code', 'product_name', 'quantity', 'description']
