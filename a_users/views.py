from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User

# Create your views here.
def profile_view(request, username=None):
    profile = request.user.profile
    return render(request, 'a_users/profile.html', {'profile': profile})
