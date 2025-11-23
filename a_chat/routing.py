# this file is like urls.py
from django.urls import path
from .consumers import *

websocket_urlpatterns = [
    path("ws/chatroom/<int:group_id>/", ChatroomConsumer.as_asgi())
]