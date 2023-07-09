from typing import Any, Dict
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.views.generic.edit import UpdateView
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.urls import reverse_lazy

from .forms import CustomUserCreationForm, UpdateUserForm
from .models import CustomUser


def register_user(request):
    page = 'register'
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = user.email.lower()
            user.save()
            login(request, user)
            messages.success(request, 'Your account was created')
            return redirect('home')
    context = {
        'form': form,
        'page': page,
    }
    return render(request, 'users/register_login.html', context)

def login_user(request):
    page = 'login'
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            CustomUser.objects.get(email=email)
        except:
            messages.error(request, 'User does not exist')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Email or password is incorrect')
    context = {
        'page': page,
    }
    return render(request, 'users/register_login.html', context)
    
def logout_user(request):
    logout(request)
    messages.info(request, 'You have been logged out')
    return redirect('login')


class UserUpdate(UpdateView):
    model = CustomUser
    form_class = UpdateUserForm
    template_name = 'users/update_user.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        return self.request.user


class UserDetail(DetailView):
    model = CustomUser
    context_object_name = 'user'
    template_name = 'users/user_profile.html'

    # def get_context_data(self, **kwargs: Any):
    #     fields_list = dict(CustomUser._meta.get_fields())
    #     fields = dict()
    #     for field in fields_list:

    #     return fields


