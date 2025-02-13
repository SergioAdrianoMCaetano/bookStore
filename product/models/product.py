from django.db import models

from product.models.category import Category


class Product(models.Model):
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.categories = None

    objects = None
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True, null=True)
    price = models.PositiveIntegerField(null=True)
    active = models.BooleanField(default=True)
    category = models.ManyToManyField(Category, blank=True)


