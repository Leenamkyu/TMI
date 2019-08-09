from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.CreateUserView.as_view(), name='signup'),
    path('signup/done/', views.RegisteredView.as_view(), name='signupdone'),
    path('profile/', views.Viewposts, name="profile"),
]