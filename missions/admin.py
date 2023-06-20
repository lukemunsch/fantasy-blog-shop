from django.contrib import admin

from .models import Mission, Update

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

@admin.register(Update)
class UpdateAdmin(admin.ModelAdmin):
    list_display = (
        'mission',
        'created_on',
        'approved',
    )
    list_filter = (
        'approved',
    )
    search_fields = [
        'mission',
        'body',
    ]

    actions = [
        'approve_update'
    ]

    def approve_update(self, request, queryset):
        queryset.update(approved=1)
