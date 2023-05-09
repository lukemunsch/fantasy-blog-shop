from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Personnel

# Register your models here.
@admin.register(Personnel)
class PersonnelAdmin(SummernoteModelAdmin):
    """set up our personnel creation form"""
    prepopulated_fields = {'slug': ('name',)}
    summernote_field = ['speciality']

    list_filter = ('rank', 'current_status')
    list_display = (
        'name',
        'age',
        'rank',
        'current_status',
    )
    search_fields = [
        'name',
        'originated_from',
        'speciality',
    ]
