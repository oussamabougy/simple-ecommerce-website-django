"""Represent the admin of the products app."""

from django.contrib import admin

from .models import Company, Category

admin.site.register(Company)
admin.site.register(Category)
