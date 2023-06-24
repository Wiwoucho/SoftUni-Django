from django.urls import path
from .views import profile_edit, profile_delete, profile_create, profile_details


urlpatterns = [
    path('create/', profile_create, name='profile create'),
    path('details/', profile_details, name='profile details'),
    path('edit/', profile_edit, name='profile edit'),
    path('delete/', profile_delete, name='profile delete'),
]