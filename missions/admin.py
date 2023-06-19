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
        'approved_mission',
    )

    list_filter = (
        'mission_grade',
        'mission_lead',
    )

    search_fields = [
        'mission',
        'description',
    ]

    actions = ['approve_mission']

    def approve_mission(self, request, queryset):
        queryset.update(approved_mission=1)
