from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from .models import Profile

def people_context(request):
    # i will change this logic to show only subscribers of user's subscribers
    # and there should be limit to display
    if request.user.is_authenticated:
        people = Profile.objects.exclude(user=request.user)
        return {'people': people}
    return {}
