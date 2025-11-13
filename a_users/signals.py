# when user is created profile is also created
from .models import Profile
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def user_postsave(sender, instance, created, **kwargs):
    user = instance

    # if new user is created then new profile is created
    if created:
        Profile.objects.create(
            user = user,
        )
# then register it in apps.py
