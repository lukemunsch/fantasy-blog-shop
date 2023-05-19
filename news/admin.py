from django.contrib import admin
from .models import News

# Register your models here.
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    """set up our admin for news entries"""
    prepopulated_fields = {
        'slug': ('news_type', 'author', 'title')
    }

    list_display = (
        'title',
        'news_type',
        'author',
        'publish_date',
    )

    list_filter = (
        'news_type',
    )

    search_fields = [
        'title',
        'author',
        'news_content',
    ]
