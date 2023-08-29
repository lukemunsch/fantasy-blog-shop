from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.view_basket, name='view_basket'),
    path('add/<product_id>/', views.add_to_basket, name='add_to_basket'),
    path('update/<product_id>/', views.update_basket, name='update_basket'),
]
