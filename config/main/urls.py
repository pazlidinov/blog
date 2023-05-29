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
    path('sort_by_title/', views.sort_by_title, name='sort_by_title'),
    
    # comment
    path('comment/<int:id>/', views.create_comment, name='comment'),
    path('comment/delete/<int:id>/', views.delete_comment, name='delete_comment'),
    
    # replay_comment
    path('replay_comment/<int:id>/', views.replay_comment, name='replay_comment'),
    path('delete_replay_comment/<int:id>/', views.delete_replay_comment, name='delete_replay_comment'),
    
]
