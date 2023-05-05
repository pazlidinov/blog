from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.home_page, name='home'),
    # Standart Auth views from Django
    path("login/", auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),
    path("logout/", auth_views.LogoutView.as_view(template_name='auth/logout.html'), name='logout'),
]