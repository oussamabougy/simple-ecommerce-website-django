"""Represent the admin of the products app."""

from django.contrib import admin

from .models import Company

admin.site.register(Company)
