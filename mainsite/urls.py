from unicodedata import name
from django.contrib import admin
from django.urls import path
from .views import about, contact, home, news, services

app_name = 'mainsite'

urlpatterns = [
    path('', home, name='home'),
    path('about/',about, name='about'),
    path('services/',services, name='services'),
    path('news/',news, name='news'),
    path('contact/', contact, name='contact'),
]