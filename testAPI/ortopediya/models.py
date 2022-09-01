from django.db import models

# Create your models here.
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'
        ordering = ["id"]


class Subcategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey('Category', on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'подкатегории'
        verbose_name_plural = 'подкатегории'
        ordering = ["category"]

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to="photos/%Y/%m/%d")
    art = models.CharField(max_length=50, default=0)
    subcategory = models.ForeignKey('Subcategory', on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product', kwargs={'id_product': self.pk})

    class Meta:
        verbose_name = 'Товары'
        verbose_name_plural = 'Товары'
        ordering = ["subcategory"]

class Store(models.Model):
    name = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    map = models.CharField(max_length=1000)
    address = models.CharField(max_length=150)
    phone = models.CharField(max_length=20, default='')
    description = models.TextField(default="", blank=False)
    image = models.ImageField(upload_to="photos/%Y/%m/%d", default="", blank=False)

    class Meta:
        verbose_name = 'Салоны'
        verbose_name_plural = 'Салоны'
        ordering = ["street"]


class Index_product(models.Model):
    id_product = models.ForeignKey('Product',  on_delete = models.CASCADE, null=True)

    class Meta:
        verbose_name = 'Продукты для слайдера главной страницы'
        verbose_name_plural = 'Продукты для слайдера главной страницы'
        ordering = ["id_product"]
