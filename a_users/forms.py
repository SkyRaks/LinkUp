from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from .models import Profile

class ProflileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['user', 'folowers']
        widgets = {
            'image': forms.FileInput(),
            'first_name': forms.TextInput(attrs={'placeholder': 'Add first name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Add last name'}),
            'info': forms.TextInput(attrs={'rows': 3, 'placeholder': 'Add info'})
        }

class EmailForm(ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['email']