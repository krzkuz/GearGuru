from django.db import models

from .model_choices import (GuitarTypeChoices, BodyTypeChoices, 
    PickupConfigurationChoices, BridgeTypeChoices, ConditionTypeChoices,
    TransactionTypeChoices)
from users.models import CustomUser



class Guitar(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    transaction_type = models.CharField(max_length=1, 
        choices=TransactionTypeChoices.choices, default=TransactionTypeChoices.SELL)
    guitar_type = models.CharField(max_length=2, choices=GuitarTypeChoices.choices)
    condition = models.CharField(max_length=3, choices=ConditionTypeChoices.choices, 
        default=ConditionTypeChoices.EXCELLENT)
    finish = models.CharField(max_length=100, null=True, blank=True)
    year_of_production = models.IntegerField(null=True, blank=True)
    frets = models.CharField(max_length=100, null=True, blank=True)
    is_right_handed = models.BooleanField(default=True, verbose_name='Right handed')
    body_type = models.CharField(max_length=2, choices=BodyTypeChoices.choices,
        null=True, blank=True)
    fretboard_material = models.CharField(max_length=100, null=True, blank=True)
    number_of_strings = models.CharField(max_length=100, null=True, blank=True)
    neck_material = models.CharField(max_length=100, null=True, blank=True)
    body_material = models.CharField(max_length=100, null=True, blank=True)
    pickup_configuration = models.CharField(max_length=3, 
        choices=PickupConfigurationChoices.choices, null=True, blank=True)
    bridge_type = models.CharField(max_length=2, choices=BridgeTypeChoices.choices,
        null=True, blank=True)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.brand = self.brand.lower().capitalize()
        self.model = self.model.lower().capitalize()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.brand} {self.model}'
    

class ElectricGuitarProxyManager(models.Manager):
    def all(self):
        return self.get_queryset().filter(guitar_type=GuitarTypeChoices.ELECTRIC)
    

class ElectricGuitarProxy(Guitar):
    objects = ElectricGuitarProxyManager()
    class Meta:
        proxy = True
        verbose_name = 'Electric Guitar'
        verbose_name_plural = 'Electric Guitars'

    def save(self, *args, **kwargs):
        self.type = GuitarTypeChoices.ELECTRIC
        super().save(*args, **kwargs)


class AcousticGuitarProxyManager(models.Manager):
    def all(self):
        return self.get_queryset().filter(guitar_type=GuitarTypeChoices.ACOUSTIC)
    

class AcousticGuitarProxy(Guitar):
    objects = AcousticGuitarProxyManager()
    class Meta:
        proxy = True
        verbose_name = 'Acoustic Guitar'
        verbose_name_plural = 'Acoustic Guitars'

    def save(self, *args, **kwargs):
        self.type = GuitarTypeChoices.ACOUSTIC
        super().save(*args, **kwargs)


class ClassicalGuitarProxyManager(models.Manager):
    def all(self):
        return self.get_queryset().filter(guitar_type=GuitarTypeChoices.CLASSICAL)
    

class ClassicalGuitarProxy(Guitar):
    objects = ClassicalGuitarProxyManager()
    class Meta:
        proxy = True
        verbose_name = 'Classical Guitar'
        verbose_name_plural = 'Classical Guitars'

    def save(self, *args, **kwargs):
        self.type = GuitarTypeChoices.CLASSICAL
        super().save(*args, **kwargs)


class BassGuitarProxyManager(models.Manager):
    def all(self):
        return self.get_queryset().filter(guitar_type=GuitarTypeChoices.BASS)
    

class BassGuitarProxy(Guitar):
    objects = BassGuitarProxyManager()
    class Meta:
        proxy = True
        verbose_name = 'Bass Guitar'
        verbose_name_plural = 'Bass Guitars'

    def save(self, *args, **kwargs):
        self.type = GuitarTypeChoices.BASS
        super().save(*args, **kwargs)

    