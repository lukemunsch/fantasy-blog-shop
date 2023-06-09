from django.contrib import admin
from .models import Personnel

# Register your models here.
@admin.register(Personnel)
class PersonnelAdmin(admin.ModelAdmin):
    """set up our personnel creation form"""
    prepopulated_fields = {'slug': ('name', 'originated_from', 'age',)}

    list_filter = ('rank', 'current_status')
    list_display = (
        'name',
        'age',
        'rank',
        'current_status',
        'authorised',
    )
    search_fields = [
        'name',
        'originated_from',
        'speciality',
    ]

    actions = ['authorise_member']

    def authorise_member(self, request, queryset):
        queryset.update(authorised=1)
