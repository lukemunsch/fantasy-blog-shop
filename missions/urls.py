from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.missions, name='missions'),
    path('<int:mission_id>/', views.mission_details, name='mission_details'),
    path('add-mission/', views.add_mission, name='add_mission'),
    path('pending-missions/', views.pending_missions, name='pending_missions'),
    path('edit-missions/<int:mission_id>', views.edit_mission, name='edit_mission'),
    path('delete-mission/<int:mission_id>', views.delete_mission, name='delete_mission'),
    path('<int:mission_id>/add-update', views.add_update, name='add_update'),
]
