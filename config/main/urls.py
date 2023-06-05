from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home_page, name='home'),
    path('list_articles/', views.List_articles.as_view(), name='list_articles'),
    path('detail/<pk>/', views.my_def, name='detail'),
    path('add/rating/', views.add_rating, name="add_rating"),
    path('add/like/', views.add_like, name="add_like"),


    # sort
    path('sort_by_teg/<slug>/', views.sort_by_teg, name='sort_by_teg'),
    path('sort_by_category/<slug>/',
         views.sort_by_category, name='sort_by_category'),
    path('sort_by_title/', views.sort_by_title, name='sort_by_title'),
    path('sort_by_author/<int:id>/', views.sort_by_author, name='sort_by_author'),
    path('sort_by_published/<str:published>/',
         views.sort_by_published, name='sort_by_published'),
    path('sort_by_like/', views.sort_by_like, name='sort_by_like'),
    path('sort_by_rating/', views.sort_by_rating, name='sort_by_rating'),

    # comment
    path('comment/<int:id>/', views.create_comment, name='comment'),
    path('comment/delete/<int:id>/', views.delete_comment, name='delete_comment'),

    # replay_comment
    path('replay_comment/<int:id>/', views.replay_comment, name='replay_comment'),
    path('delete_replay_comment/<int:id>/',
         views.delete_replay_comment, name='delete_replay_comment'),

]
