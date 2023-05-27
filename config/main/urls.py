from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home_page, name='home'),
    
]
