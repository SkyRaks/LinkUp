from django.urls import path
from .views import *

urlpatterns = [
    path('', home_view, name='home'),
    path('create_post/', create_post, name='create-post'),
]