import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string

from .models import *


class ChatroomConsumer(WebsocketConsumer):
    def connect(self):
        self.user = self.scope['user']
        self.group_id = self.scope['url_route']['kwargs']['group_id']
        try:
            self.chatroom = ChatGroup.objects.get(id=self.group_id)
        except ChatGroup.DoesNotExist:
            return self.close()

        self.group_name = str(self.group_id)

        async_to_sync(self.channel_layer.group_add)(
            self.group_name, self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.group_name, self.channel_name
        )

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        body = text_data_json['body']
        # print(body)

        message = ChatMessage.objects.create(
            body = body,
            author = self.user,
            group = self.chatroom
        )

        event = {
            'type': 'message_handler',
            'message_id': message.id
        }

        async_to_sync(self.channel_layer.group_send)(
            self.group_name, event
        )

    def message_handler(self, event):
        message_id = event['message_id']
        message = ChatMessage.objects.get(id=message_id)
        context = {
            'message': message,
            'user': self.user,
        }
        html = render_to_string("a_chat/partials/chat_message_partial.html", context=context)
        self.send(text_data=html)