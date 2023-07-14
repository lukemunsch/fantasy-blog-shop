from django.contrib import admin

from .models import Category

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    """set up our display in admin for categories"""
    list_display = ('name', 'friendly_name',)

admin.site.register(Category, CategoryAdmin)
