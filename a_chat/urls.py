from django.urls import path
from .views import *

urlpatterns = [
    # path('chat/', chat_view, name='chat'),
    path('chat/<str:username>/', chat_view, name='chat'),
]