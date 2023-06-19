from django.contrib import admin

from .models import Mission, MissionUpdate

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


@admin.register(MissionUpdate)
class MissionUpdateAdmin(admin.ModelAdmin):
    """set up our admin page for Comments"""
    list_display = ('name', 'mission', 'created_on',)
    search_fields = ['mission', 'name', 'body',]

    actions = ['approve_update']

    def approve_update(self, request, queryset):
        queryset.update(approve_update=1)
