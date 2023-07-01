from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):

    def create_user(self, email, username, password=None):
        if email is None:
            raise TypeError('Users must have an email address.')
        if username is None:
            raise TypeError('Users must have a username.')
        user = self.model(
            email=self.normalize_email(email),
            username=username
            )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=email,
            password=password,
            username=username
            )
        user.is_superuser = True
        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(blank=False, null=False, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    country = models.CharField(max_length=50, null=True, blank=False)
    city = models.CharField(max_length=150, null=True, blank=False)
    street = models.CharField(max_length=150, null=True, blank=False)
    apartment = models.CharField(max_length=50, null=True, blank=False)
    zip_code = models.CharField(max_length=50, null=True, blank=False)
    last_active = models.DateTimeField(auto_now=True)
    joined = models.DateTimeField(auto_now_add=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    # reviews = models.ForeignKey()
    # messages = models.ForeignKey()
    # instruments = models.ForeignKey()

    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username


