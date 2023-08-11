from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.resources, name='resources'),
    path('pending-resources/', views.pending_resources, name='pending_resources'),
    path('resource-details/<slug:slug>/', views.resource_details, name='resource_details'),
    path('add_resource/', views.add_resource, name='add_resource'),
    path('edit_resource/<slug:slug>', views.edit_resource, name='edit_resource'),
    path('delete_resource/<slug:slug>/', views.delete_resource, name='delete_resource'),
]
