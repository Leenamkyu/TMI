
from django.contrib import admin
from django.urls import path, include
import AppMain.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', AppMain.views.home, name='home'),              # home page
    path('userboard/', include('AppUserboard.urls')),       # Userboard page
    path('accounts/', include('AppAccount.urls')),          # signup
    path('accounts/',include('django.contrib.auth.urls')),  # login and logout
    path('recommend/', include('AppRecommend.urls')),       # recommend page
]
