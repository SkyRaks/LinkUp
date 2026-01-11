# from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from a_users.models import *
from .forms import *
from django.core.cache import cache

# Create your views here.

@login_required
def home_view(request):
    cache_key = "home_post_feed"

    if Post.objects.all():
        post_feed = cache.get("home_post_feed")

        if not post_feed:
            print("loading posts")
            post_feed = Post.objects.all()
            cache.set(cache_key, post_feed, timeout=60)
        else: #this else statement is check if this thing is working
            print("cache hit!")
        myFolowers = request.user.profile.folowers.all()

        people = set() # people you may know set

        if myFolowers.exists():

            for myFolower in myFolowers: # looping through every folower
                folowers = myFolower.profile.folowers.all() # getting my folowers folower

                for person in folowers:
                    if person == request.user or person in myFolowers or request.user in person.profile.folowers.all():
                        continue
                    people.add(person.profile)
        else:
            from django.contrib.auth import get_user_model
            User = get_user_model()
            otherPeople = User.objects.all()
            otherPeople = User.objects.exclude(id=request.user.id)

            for otherPerson in otherPeople:
                people.add(otherPerson.profile)

        print("people: ", people)

        return render(request, 'home.html', {'post_feed': post_feed, 'folowers': myFolowers, 'people': people})
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
    post = get_object_or_404(Post, id=post_id)

    if new_like in post.likes.all():
        post.likes.remove(new_like)
    else:
        post.likes.add(new_like)

    post.refresh_from_db()
    return render(request, 'partials/like_button_partial.html', {'post': post})

