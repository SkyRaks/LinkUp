from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

@login_required
def people_context(request):
    # i will change this logic to show only subscribers of user's subscribers
    # and there should be limit to display
    User = get_user_model()
    people = User.objects.all()
    return {'people': people}
