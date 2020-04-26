"""Represent Django tests."""

import datetime

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Product, Company, Category


def create_product(name, description, days, company):
    """
    Create a product with the given `product_name` and publishing_end_date in
    form of `days` offset to now.
    """
    time = timezone.now() + datetime.timedelta(days=days)
    product = Product.objects.create(name=name, description=description,
                                     company=company,
                                     school_type='PR', price=12.34,
                                     publishing_end_date=time)

    category1 = Category.objects.create(name='bags')
    product.categories.add(category1)
    return product


class ProductListViewTests(TestCase):
    """Run product listing tests."""

    @classmethod
    def setUpTestData(cls):
        # Set up data for the whole TestCase
        cls.company = Company.objects.create(name='Techno')

    def test_no_products(self):
        """
        If no product exist, return no product message.
        """
        response = self.client.get(reverse('list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No products are available.")
        self.assertQuerysetEqual(response.context['product_list'], [])

    def test_past_and_future_publishing_end_date(self):
        """
        Show only products with the publishing_end_date is in the future.
        """
        create_product(name="Ruler", description='School ruler 30cm', days=-3,
                       company=self.company)
        create_product(name="School Bag", description='bag', days=5,
                       company=self.company)
        response = self.client.get(reverse('list'))
        self.assertQuerysetEqual(
            response.context['product_list'],
            ['<Product: School Bag>']
        )


class ProductDetailViewTests(TestCase):
    """Run product detail tests."""

    @classmethod
    def setUpTestData(cls):
        # Set up data for the whole TestCase
        cls.company = Company.objects.create(name='Techno')

    def test_product_does_not_exist(self):
        """
        If no product exist with the given id, return 404 not found.
        """
        url = reverse('detail', args=(40,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_and_future_publishing_end_date(self):
        """
        Show only products with the publishing_end_date is in the future.
        """
        product1 = create_product(name="Ruler",
                                  description='School ruler 30cm', days=3,
                                  company=self.company)
        product2 = create_product(name="School Bag", description='bag',
                                  days=-5, company=self.company)
        response1 = self.client.get(reverse('detail', args=(product1.id,)))
        response2 = self.client.get(reverse('detail', args=(product2.id,)))
        self.assertContains(response1, product1.name)
        self.assertEqual(response2.status_code, 404)
