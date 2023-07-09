from django.db import models

from users.models import CustomUser
from gear.models import Guitar


class Image(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    message = models.ForeignKey('Message', on_delete=models.CASCADE, null=True, 
        blank=True)
    

class Message(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField(null=True, blank=True)
    is_read = models.BooleanField(default=False)
    time_stamp = models.DateTimeField(auto_now_add=True)
    related_gear = models.ForeignKey(Guitar, on_delete=models.SET_NULL, null=True,
        blank=True)
    from_user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL,
        related_name='message_from', null=True)
    to_user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL,
        related_name='message_to', null=True)

    def __str__(self):
        return self.title