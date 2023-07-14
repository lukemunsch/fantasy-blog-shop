from django.contrib import admin

from .models import Category, Product

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """set up our display in admin for categories"""
    list_display = ('name', 'friendly_name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """set up our admin"""
    list_display = (
        'name',
        'price',
        'category',
        'approved_item',
    )
    list_filter = (
        'category',
        'approved_item',
    )
    search_fields = [
        'name',
        'price',
    ]

    actions = ['authorise_item']

    def authorise_item(self, request, queryset):
        """set up our new function for additinoal action"""
        queryset.update(approved_item=1)
