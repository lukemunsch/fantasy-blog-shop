from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('pending-articles/', views.pending_articles, name='pending_articles'),
    path('pending-missions/', views.pending_missions, name='pending_missions'),
    path('pending-members/', views.pending_members, name='pending_members'),
]
