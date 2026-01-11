from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProflileForm, EmailForm
from .models import *
from allauth.account.models import EmailAddress
from django.contrib.auth import logout

# Create your views here.
def profile_view(request, username=None):
    if username:
        profile = get_object_or_404(User, username=username).profile
        profile_posts = Post.objects.filter(author=profile.user)
        post_count = profile_posts.count()
    else:
        profile = request.user.profile
        profile_posts = Post.objects.filter(author=request.user)
        post_count = profile_posts.count()
    return render(request, 'a_users/profile.html', {'profile': profile, 'profile_posts': profile_posts, 'post_count': post_count})

def get_post_view(request, id):
    post = Post.objects.get(pk=id)
    return render(request, 'a_users/selected_post.html', {'post': post})

def folow_list_view(request, mode, username):
    thisUser = get_object_or_404(User, username=username)

    if mode == 'folowers':
        thisFolowers = thisUser.profile.folowers.all()
    elif mode == 'folowing':
        thisFolowers = thisUser.subscribers.all()

    return render(request, 'a_users/folowers_list.html', {'thisFolowers': thisFolowers, 'mode': mode})

def folow_view(request, username):
    new_folower = request.user
    thisUser = get_object_or_404(User, username=username)

    # this user's folowers
    if new_folower in thisUser.profile.folowers.all():
        thisUser.profile.folowers.remove(new_folower)
        return redirect(f"/profile/{thisUser.profile}/")

    # user who folows the other one^
    thisUser.profile.folowers.add(new_folower)

    return redirect(f"/profile/{thisUser}/")

@login_required
def profile_edit_view(request):
    form = ProflileForm(instance=request.user.profile)
    if request.method == 'POST':
        form = ProflileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    return render(request, 'a_users/profile_edit.html', {'form': form})

def profile_settings_view(request):
    return render(request, 'a_users/profile_settings.html')

@login_required
def profile_email_change(request):
    if request.htmx:
        form = EmailForm(instance=request.user)
        return render(request, 'partials/email_form.html', {'form':form})

    if request.method == 'POST':
        form = EmailForm(request.POST, instance=request.user)
        if form.is_valid():
            email = form.cleaned_data['email']
            if User.objects.filter(email=email).exclude(id=request.user.id).exists():
                print("already exists")
                return redirect('profile-settings')
            form.save()
            send_email_confirmation(request, email)
            return redirect('profile-settings')
        else:
            print("form is not valid")
            return redirect('profile-settings')
    return redirect('home')

def send_email_confirmation(request, email):
    email_obj, created = EmailAddress.objects.get_or_create(
        user=request.user,
        email=email,
        defaults={'primary': True}
    )

    # Mark it unverified (in case user changed email)
    email_obj.verified = False
    email_obj.save()

    # Send confirmation email
    email_obj.send_confirmation(request)

@login_required
def profile_email_verify(request):
    send_email_confirmation(request, request.user.email)
    return redirect('profile-settings')

def profile_delete_view(request):
    user = request.user
    if request.method == 'POST':
        logout(request)
        user.delete()
        # messages.success(request, 'Account deleted, how sad...(no)')
        return redirect('home')

    return render(request, 'users/profile_delete.html')
