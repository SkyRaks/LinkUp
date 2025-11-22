from django.forms import ModelForm
from django import forms
from .models import *

class ChatMessageForm(ModelForm):
    class Meta:
        model = ChatMessage
        fields = ['body']
        widgets = {
            'body': forms.TextInput(attrs={'placeholder': 'add message',
                                           'class': 'form-control text-black',
                                           'max_length': '300',
                                           'autofocus': True})}
