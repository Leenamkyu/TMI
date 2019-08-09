
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='recommend_main'), # recommend main page 
    path('newpost/', views.create, name='recommend_new'), # recommend new post form page
    path('update/<int:postID>', views.update, name='recommend_update'), # recommend update
    path('delete/<int:postID>', views.delete, name='recommend_delete'), # recommend delete
    path('detail/<int:postID>', views.detail, name='recommend_detail'), # recommend detail
    path('like/', views.like, name='recommend_like'), # recommend like
    path('comment/', views.create_comment, name='recommend_comment'), # recommend comment
    path('comment/<int:postID>/remove/<int:cpk>', views.remove_comment, name='recommend_comment_remove'), # recommend comment remove
]
