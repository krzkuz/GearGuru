from django.db import models

from gear.models import Guitar


class Exchange(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    brand = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)
    more_info = models.TextField(verbose_name='More informations')
    related_gear = models.ForeignKey(Guitar, on_delete=models.CASCADE, 
        related_name='exchange_for')
    
    def save(self, *args, **kwargs):
        if not self.title:
            self.title = f'{self.related_gear.brand} {self.related_gear.model} to exchange'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Rent(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    price = models.IntegerField(null=True, blank=True)
    renting_time = models.IntegerField(null=True, blank=True, 
        verbose_name='Renting time in days')
    more_info = models.TextField(verbose_name='More informations')
    related_gear = models.OneToOneField(Guitar, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.title:
            self.title = f'{self.related_gear.brand} {self.related_gear.model} for rent'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Sell(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    price = models.IntegerField(null=True, blank=True)
    more_info = models.TextField(verbose_name='More informations')
    related_gear = models.OneToOneField(Guitar, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.title:
            self.title = f'{self.related_gear.brand} {self.related_gear.model} for sell'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Image(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to='')
    guitar = models.ForeignKey(Guitar, on_delete=models.CASCADE, null=True, 
        blank=True)
    
    @property
    def image_url(self):
        try: 
            url = self.image.url
        except:
            url = ''
        return url    