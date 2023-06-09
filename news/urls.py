from django.urls import path

from . import views

urlpatterns = [
    path('', views.news, name='news'),
    path('<int:news_id>/', views.news_details, name='news_details'),
    path('add-news/', views.add_news, name='add_news'),
    path('pending-articles/', views.pending_articles, name='pending_articles'),
    path('edit-news/<int:news_id>', views.edit_news, name='edit_news'),
    path('delete-news/<int:news_id>', views.delete_news, name='delete_news'),
]
