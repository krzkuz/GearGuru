from django.urls import path

from . import views


urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('<int:pk>/', views.AdvertisementView.as_view(), name='guitar'),
    path('electric-guitars/', views.ElectricGuitarsView.as_view(), name='electric-guitars'),
    path('bass-guitars/', views.BassGuitarsView.as_view(), name='bass-guitars'),
    path('acoustic-guitars/', views.AcousticGuitarsView.as_view(), name='acoustic-guitars'),
    path('classical-guitars/', views.ClassicalGuitarsView.as_view(), name='classical-guitars'),




]