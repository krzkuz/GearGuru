from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
            if name == 'password1':
                name = 'Password'
            if name == 'password2':
                name = 'Confirm password'
            field.widget.attrs.update({'placeholder': name.capitalize()})

class UpdateUserForm(ModelForm):
    class Meta:
        model = CustomUser
        exclude = ['email', 'password', 'is_staff', 'is_active', 'is_superuser',
                   'last_login', 'user_permissions', 'groups', 'average_rating']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            name = name.replace('_', ' ')
            field.widget.attrs.update({'class': 'input'})
            field.widget.attrs.update({'placeholder': name.capitalize()})
