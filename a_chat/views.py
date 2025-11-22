from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import *

# Create your views here.
@login_required
def chat_view(request, username):
    if request.user.username == username:
        print('are u retarted?')
        return redirect('home')

    other_user = User.objects.get(username=username)
    my_chatrooms = request.user.chat_groups.all()

    chatroom = None

    for room in my_chatrooms:
        if other_user in room.members.all():
            chatroom = room
            break

    if chatroom == None:
        chatroom = ChatGroup.objects.create()
        chatroom.members.add(other_user, request.user)

    chat_messages = chatroom.chat_messages.all()[:30]

    return render(request, 'a_chat/chat.html', {'chat_messages': chat_messages})
