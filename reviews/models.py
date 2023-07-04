from django.db import models
from users.models import CustomUser


class RateChoices(models.TextChoices):
    FIVE = '5', 'Five stars'
    FOUR = '4', 'Four stars'
    THREE = '3', 'Three stars'
    TWO = '2', 'Two stars'
    ONE = '1', 'One star'


class Review(models.Model):
    rate = models.CharField(max_length=1, choices=RateChoices.choices)
    description = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    from_user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, 
        null=True, related_name='from_user')
    to_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,
        null=True, related_name='to_user')

