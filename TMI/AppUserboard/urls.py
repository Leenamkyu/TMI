from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='userboard_main'), # user board main page
]