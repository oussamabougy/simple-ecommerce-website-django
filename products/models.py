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
