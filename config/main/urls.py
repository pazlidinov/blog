from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home_page, name='home'),
    path('list_articles/', views.List_articles.as_view(), name='list_articles'),
    path('detail/<pk>/', views.Detail_Article.as_view(), name='detail'),
   
    
    # sort
    path('sort_by_teg/<slug>/', views.sort_by_teg, name='sort_by_teg'),
    path('sort_by_category/<slug>/', views.sort_by_category, name='sort_by_category'),
    
]
