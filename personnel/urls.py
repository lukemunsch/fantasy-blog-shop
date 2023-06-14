from django.urls import path

from . import views

urlpatterns = [
    path('', views.personnel, name='personnel'),
    path(
        '<int:personnel_id>/',
        views.personnel_details,
        name='personnel_details'
    ),
    path(
        'add-member/',
        views.add_member,
        name='add_member'
    ),
    path('pending-members/', views.pending_members, name='pending_members'),
    path('edit-member/<int:personnel_id>', views.edit_member, name='edit_member'),
]
