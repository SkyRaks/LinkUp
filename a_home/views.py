from django.shortcuts import render, get_object_or_404, redirect
from a_users.models import *
from .forms import *

# Create your views here.

def home_view(request):
    if Post.objects.all():
        post_feed = Post.objects.all()
        return render(request, 'home.html', {'post_feed': post_feed})
    else:
        return redirect(request, 'home')

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home')
    else:
        form = PostForm
    return render(request, 'a_home/create_post.html', {'form': form})
