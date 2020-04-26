"""Represent the admin of the products app."""

from django.contrib import admin

from .models import Company, Category, Product
from .forms import ProductForm


class ProductAdmin(admin.ModelAdmin):
    """Make custom product admin model."""
    form = ProductForm
    list_display = ('name', 'price')


admin.site.register(Company)
admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
