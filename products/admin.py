from django.contrib import admin
from .models import Product, Image, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'created')
    list_filter = ['created']
    search_fields = ('name', 'slug')
    readonly_fields = ('created', 'slug')



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'created')
    list_filter = ['created']
    search_fields = ('name', 'description')
    ordering = ('-created',)
    readonly_fields = ('created', 'slug')



@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('product', 'image')
