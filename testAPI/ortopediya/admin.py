from django.contrib import admin

# Register your models here.
from .models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'art', 'subcategory')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'art')
    list_filter = ('subcategory',)


class StoreAdmin(admin.ModelAdmin):
    list_display = ('id', 'street', 'address')
    list_display_links = ('id', 'street')
    search_fields = ('street',)
    list_filter = ('street',)


class Index_productAdmin(admin.ModelAdmin):
    list_display = ('id_product', )


class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')



admin.site.register(Category)
admin.site.register(Subcategory, SubcategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(Index_product, Index_productAdmin)
