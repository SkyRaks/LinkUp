from django.db import models
from django.contrib.auth.models import User
from django.templatetags import static

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    info = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='avatars/', null=True, blank=True)

    def __str__(self):
        return str(self.user)

    @property
    def name(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        elif self.first_name:
            return self.first_name
        # elif self.last_name:
        #     return self.last_name
        return self.user.username

    @property
    def avatar(self):
        try:
            avatar = self.image.url
        except:
            # default avatar
            avatar = static('images/Default_pfp.jpg')
        return avatar
