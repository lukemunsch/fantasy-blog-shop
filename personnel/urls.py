from django.urls import path

from . import views

urlpatterns = [
    path('', views.personnel, name='personnel'),
    path(
        '<int:personnel_id>/',
        views.personnel_details,
        name='personnel_details'
    ),
]
