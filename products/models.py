"""Represent Django models."""

from django.db import models


class Company(models.Model):
    """Represents a company inside our system."""
    name = models.CharField(max_length=120)
    logo = models.ImageField(upload_to='logos/', null=True)

    class Meta:
        verbose_name_plural = 'companies'

    def __str__(self):
        """Return the model as a string."""
        return self.name


class Category(models.Model):
    """Represents a category inside our system."""
    name = models.CharField(max_length=120)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        """Return the model as a string."""

        return self.name


class Product(models.Model):
    """Represents a product inside our system."""

    SCHOOL_TYPE = [
        ('PR', 'praktijkonderwijs'),
        ('VM', 'vmbo'),
        ('MB', 'mbo'),
        ('HB', 'hbo'),
        ('OP', 'opleidingsbedrijf'),
    ]

    name = models.CharField(max_length=120)
    image = models.ImageField(upload_to='product_images/', null=True)
    description = models.TextField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    school_type = models.CharField(max_length=2, choices=SCHOOL_TYPE)
    price = models.FloatField()
    publishing_end_date = models.DateTimeField()

    class Meta:
        ordering = ['id']

    def __str__(self):
        """Return the model as a string."""

        return self.name
