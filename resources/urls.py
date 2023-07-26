from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.resources, name='resources'),
    path('pending-resources/', views.pending_resources, name='pending_resources'),
    path('resource-details/<slug:slug>', views.resource_details, name='resource_details'),
]
