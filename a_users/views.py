from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User

# Create your views here.
def profile_view(request):
    profile = request.user.profile
    return render(request, 'a_users/profile.html', {'profile': profile})

def profile_edit_view(request):
    return render(request, 'a_users/profile_edit.html')
