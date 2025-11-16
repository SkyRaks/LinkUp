# when user is created profile is also created
from .models import Profile
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from allauth.account.models import EmailAddress

@receiver(post_save, sender=User)
def user_postsave(sender, instance, created, **kwargs):
    user = instance

    # if new user is created then new profile is created
    if created:
        Profile.objects.create(
            user = user,
        )
    else:
        try:
            email_address = EmailAddress.objects.get_primary_email(user)
            if email_address != user.email:
                email_address = user.email
                email_address.save()
        except:
            EmailAddress.objects.create(
                user=user,
                email=user.email,
                primary=True
            )
# then register it in apps.py
