from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import *

def chat_view(request):
    return render(request, 'a_chat/chat.html')
# Create your views here.
@login_required
def get_or_create_chatroom(request, username):
    if request.user.username == username:
        print('are u retarted?')
        return redirect('home')

    other_user = User.objects.get(username=username)
    my_chatrooms = request.user.chatgroup.all()

    # if my_chatrooms.exists():
    for chatroom in my_chatrooms:
        if other_user in chatroom.members.all():
            chatroom = chatroom
            break
        else:
            chatroom = ChatGroup.objects.create()
            chatroom.members.add(other_user, request.user)
    return redirect('chatroom', chatroom.chat_name)
