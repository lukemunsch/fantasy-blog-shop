from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.console, name='console'),
    path('add-entries/', views.console_add_entry, name='console_add_entry'),
    path('pending-entries/', views.console_pending_entries, name='console_pending'),
]
