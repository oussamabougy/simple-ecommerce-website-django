"""Represent Django views"""

from django.views.generic import (
    ListView,
    DetailView
)
from django.utils import timezone

from .models import Product


class ProductListView(ListView):
    """Represent product list view."""
    model = Product
    paginate_by = 6

    def get_queryset(self):
        """Return the available products."""
        return Product.objects.filter(publishing_end_date__gt=timezone.now())


class ProductDetailView(DetailView):
    """Represent product detail view."""

    def get_queryset(self):
        """
        Excludes any product with expired publishing_end_date.
        """
        return Product.objects.filter(publishing_end_date__gt=timezone.now())
