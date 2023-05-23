from django.contrib import admin

from .models import Mission

# Register your models here.
@admin.register(Mission)
class MissionAdmin(admin.ModelAdmin):
    list_display = (
        'mission',
        'mission_grade',
        'mission_lead',
        'mission_length',
    )

    list_filter = (
        'mission_grade',
        'mission_lead',
    )

    search_fields = [
        'mission',
        'description',
    ]
