from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    info = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='avatars/', null=True, blank=True)
    folowers = models.ManyToManyField(User, related_name='subscribers', blank=True)

    def __str__(self):
        return str(self.user)

    @property
    def name(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        elif self.first_name:
            return self.first_name
        return self.user.username

    @property
    def avatar(self):
        if self.image:
            return self.image.url
        return f'{settings.STATIC_URL}images/avatar.svg'

# class Folowers(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     folowers = models.CharField(max_length=100)
#     folowers = models.ManyToManyField(User, related_name='subscribers', blank=True)
#
#     def __str__(self):
#         return str(self.user)