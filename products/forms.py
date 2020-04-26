"""Represent Django forms"""

from django import forms
from django.core.exceptions import ValidationError

from .models import Product


class ProductForm(forms.ModelForm):
    """Make a custom product modal form."""
    class Meta:
        model = Product
        fields = '__all__'

    def clean(self):
        super().clean()
        # Verify that product has maximum of six categories.
        categories = self.cleaned_data.get('categories')
        if categories and categories.count() > 6:
            self.add_error('categories', ValidationError(
                'Maximum of six categories are allowed'))
        return self.cleaned_data
