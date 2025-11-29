from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from a_users.models import *

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('image', 'caption')
        widgets = {
            'image': forms.FileInput(attrs={'required': True}),
            'caption': forms.TextInput(attrs={'placeholder': 'Add Caption'}),
        }

        # author = models.ForeignKey(User, on_delete=models.CASCADE)
        # image = models.ImageField(upload_to='posts_images/', null=True, blank=False)  # required
        # likes = models.ManyToManyField(User, related_name='like', blank=True)
        # caption = models.TextField(null=True, blank=True)
        # created = models.DateField(auto_now_add=True)

# class EmailForm(ModelForm):
#     email = forms.EmailField(required=True)
#
#     class Meta:
#         model = User
#         fields = ['email']