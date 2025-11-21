from django.contrib.auth.models import User
from django.db import models
import shortuuid

# Create your models here.
class ChatGroup(models.Model):
    chat_name = models.CharField(max_length=128, unique=True, default=shortuuid.uuid)
    members = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.chat_name

class ChatMessage(models.Model):
    group = models.ForeignKey(ChatGroup, related_name='chat_messages', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.CharField(max_length=300)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author.username}: {self.body}"

    class Meta:
        ordering = ['-created']
