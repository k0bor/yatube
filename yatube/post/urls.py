from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='post.index'),
     path('group/<slug:slug>/', views.group_posts, name='group_posts'),
]