from django.db.models.signals import post_save

from .models import Guitar
from advertisement.models import Sell, Exchange, Rent
from .model_choices import TransactionTypeChoices


def new_ad(sender, instance, created, **kwargs):
    if created:
        ad_type = instance.transaction_type
        if ad_type == TransactionTypeChoices.SELL:
            Sell.objects.create(related_gear=instance)
        elif ad_type == TransactionTypeChoices.EXCHANGE:
            Exchange.objects.create(related_gear=instance)
        else:
            Rent.objects.create(related_gear=instance)

post_save.connect(new_ad, sender=Guitar)
