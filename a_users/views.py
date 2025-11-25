from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProflileForm, EmailForm
from .models import *

# Create your views here.
def profile_view(request, username=None):
    if username:
        profile = get_object_or_404(User, username=username).profile
        print(f"this is profile of: {username}")
        return render(request, 'a_users/profile.html', {'profile': profile})
    else:
        profile = request.user.profile
    return render(request, 'a_users/profile.html', {'profile': profile})

def folow_view(request, username):
    new_folower = request.user.username
    thisUser = get_object_or_404(User, username=username)
    print(f"new folower: {new_folower}")
    print(f"this user: {thisUser}")
    # subs = Folowers.objects.create(user=thisUser, folowers=new_folower)
    # subs.save()
    return redirect(f"/profile/{thisUser.profile}/")

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
            return redirect('profile-settings')
        else:
            print("form is not valid")
            return redirect('profile-settings')
    return redirect('home')
