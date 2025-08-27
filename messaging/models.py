from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages_sent')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages_received')
    subject = models.CharField(max_length=120)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.subject} ({self.sender} → {self.recipient})"
