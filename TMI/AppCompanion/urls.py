from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.main, name = "companion_main"),  # companion main page
    path('new/', views.new, name = "companion_new"), # companion new page
    path('search/', views.search, name="companion_search"),
    path('update/<int:pk>', views.update, name = "companion_update"),
    path('delete/<int:pk>', views.delete, name = "companion_delete"),  #새로 추가한 부분 
 ]