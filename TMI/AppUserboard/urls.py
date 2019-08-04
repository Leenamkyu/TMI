from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='userboard_main'),    # userboard main page
    path('new/', views.new, name='userboard_new'),  # userboard new page
]