from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='userboard_main'),    # userboard main page
    path('new/', views.new, name='userboard_new'),  # userboard new page
    path('detail/<int:board_id>', views.detail, name="userboard_detail"),
    path('detail/<int:board_id>/delete/', views.delete, name="userboard_delete"),
    path('detail/<int:board_id>/update/', views.update, name="userboard_update"),
    path('searchtitle/', views.searchtitle, name='searchtitle'),
    path('searchtext/', views.searchtext, name='searchtext'),
    path('warning/', views.warning, name='warning'),
]