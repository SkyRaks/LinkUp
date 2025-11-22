from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *

# Create your views here.
@login_required
def chat_view(request, username):
    if request.user.username == username:
        print('are u retarted?')
        return redirect('home')

    # other_user = User.objects.get(username=username)
    other_user = get_object_or_404(User, username=username)
    my_chatrooms = request.user.chat_groups.all()
    chatroom = None


    for room in my_chatrooms:
        if other_user in room.members.all():
            chatroom = room
            break

    if chatroom == None:
        chatroom = ChatGroup.objects.create()
        chatroom.members.add(other_user, request.user)
    # at this point we found or created chatroom
    chat_messages = chatroom.chat_messages.all()[:30]

    form = ChatMessageForm()
    # if this is post method
    # method == 'POST'
    if request.htmx:
        form = ChatMessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.author = request.user
            message.group = chatroom
            message.save()
            # return redirect('chat', username=username) this is for posts method
            context = {
                'message': message,
                'user': request.user,
                'other_user': other_user
            }
            return render(request, 'a_chat/partials/chat_message_partial.html', context=context)

    return render(request, 'a_chat/chat.html',
                  {'chat_messages': chat_messages,
                   'form': form,
                   'other_user': other_user})
