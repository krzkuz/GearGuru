from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.views.generic import UpdateView, DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .forms import CustomUserCreationForm, UpdateUserForm
from .models import CustomUser
from gear.models import Guitar


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


class UserUpdate(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = UpdateUserForm
    template_name = 'users/update_user.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        return self.request.user


class UserDetail(LoginRequiredMixin, DetailView):
    model = CustomUser
    context_object_name = 'user'
    template_name = 'users/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        user = self.request.user
        users_gear = user.guitar_set.all()
        context['gear'] = users_gear
        return context
    
    # def get(self, request, *args, **kwargs):
    #     self.object = self.get_object()
    #     if self.request.user == self.object:
    #         return self.get_context_data(*args, **kwargs)
    #     else:
    #         users_profile = False
    #         return self.get_context_data(users_profile, **kwargs)

    # def handle_no_permission(self):
    #     messages.info(self.request, 'You have no permission to do that')
    #     return redirect('login')

class UserAdvertisments(ListView):
    model = Guitar
    template_name = 'advertisement/guitars_list.html'
    context_object_name = 'guitars'

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        queryset = queryset.filter(owner=user)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['user'] = user
        return context
