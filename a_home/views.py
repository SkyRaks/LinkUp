from django.shortcuts import render, get_object_or_404, redirect
from a_users.models import *
from .forms import *

# Create your views here.

def home_view(request):
    if Post.objects.all():
        post_feed = Post.objects.all()
        return render(request, 'home.html', {'post_feed': post_feed})
    else:
        return render(request, 'home.html')

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

def like_post(request, post_id):
    new_like = request.user
    this_post = get_object_or_404(Post, id=post_id)
    if new_like in this_post.likes.all():
        this_post.likes.remove(new_like)
        return redirect('home')
    else:
        this_post.likes.add(new_like)
        return redirect('home')
    return redirect('home')



