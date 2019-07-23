
from django.contrib import admin
from django.urls import path, include
import AppMain.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', AppMain.views.home, name='home'), # home page
]
