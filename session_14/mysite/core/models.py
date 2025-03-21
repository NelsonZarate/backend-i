from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)  # Category name
    slug = models.SlugField(max_length=255, unique=True)  # URL-friendly identifier

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="products",
        default=1
        )

    def __str__(self):
        return self.name

