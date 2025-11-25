from django.urls import path
from .views import *

urlpatterns = [
    path('', profile_view, name='profile'),
    path('edit/', profile_edit_view, name='profile-edit'),
    path('settings/', profile_settings_view, name='profile-settings'),
    path('emailchange/', profile_email_change, name='profile-emailchange'),
    path('folow/<str:username>/', folow_view, name='folow'),
]