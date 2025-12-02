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

def like_post(request, author):
    new_like = request.user
    this_user = get_object_or_404(User, username=author)
    this_posts = get_object_or_404(Post, author=this_user)

    this_posts.likes.add(new_like)

    return redirect('home')



