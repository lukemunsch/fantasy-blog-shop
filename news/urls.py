from django.urls import path

from . import views

urlpatterns = [
    path('', views.news, name='news'),
    path('<int:news_id>/', views.news_details, name='news_details')
]
