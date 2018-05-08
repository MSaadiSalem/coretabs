from django.db import models
from django.utils.text import slugify
from django.urls import reverse_lazy


class Category(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True, max_length=256)
    slug = models.SlugField(unique=True, blank=True)

    class Meta:
        ordering = ('name', '-created_at',)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)
    slug = models.SlugField(blank=True)

    category = models.ForeignKey(
        Category, related_name="products", on_delete=models.CASCADE)

    class Meta:
        ordering = ('name', 'price', '-created_at')

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse_lazy('shop:product_detail', args=(self.slug, self.id))

    def __str__(self):
        return "{0} {1}".format(self.name, self.stock)
