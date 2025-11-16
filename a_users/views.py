from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProflileForm, EmailForm

# Create your views here.
def profile_view(request):
    profile = request.user.profile
    return render(request, 'a_users/profile.html', {'profile': profile})

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
