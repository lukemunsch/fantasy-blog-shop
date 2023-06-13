from django.urls import path

from . import views

urlpatterns = [
    path('', views.news, name='news'),
    path('<int:news_id>/', views.news_details, name='news_details'),
    path('add-news/', views.add_news, name='add_news'),
    path('pending-articles/', views.pending_articles, name='pending_articles'),
]
