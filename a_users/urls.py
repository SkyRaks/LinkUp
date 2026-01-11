from django.urls import path
from .views import *

urlpatterns = [
    path('', profile_view, name='profile'),
    path('edit/', profile_edit_view, name='profile-edit'),
    path('settings/', profile_settings_view, name='profile-settings'),
    path('emailchange/', profile_email_change, name='profile-emailchange'),
    path('emailverify/', profile_email_verify, name="profile-emailverify"),
    path('folow/<str:username>/', folow_view, name='folow'),
    path('get-post/<id>/', get_post_view, name='get-post'),
    path('folow-list/<mode>/<username>/', folow_list_view, name='folow-list'),
    path('delete/', profile_delete_view, name="profile-delete"),
]