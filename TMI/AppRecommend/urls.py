
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='recommend_main'), # recommend main page 
    path('new/', views.new, name='recommend_new'), # recommand new post form page
    path('create/', views.create, name='recommend_create'), # recommend create
    path('detail/<int:postID>', views.detail, name='recommend_detail'), # recommend detail
]
