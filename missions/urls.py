from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.missions, name='missions'),
    path('<int:mission_id>', views.mission_details, name='mission_details'),
]
