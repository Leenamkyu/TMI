from django.contrib import admin
from django.urls import path, include
import AppMain.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', AppMain.views.home, name='home'),              # home page
    path('userboard/', include('AppUserboard.urls')),       # Userboard page
    path('accounts/', include('AppAccount.urls')),          # signup
    path('accounts/',include('django.contrib.auth.urls')),  # login and logout
    path('recommend/', include('AppRecommend.urls')),       # recommend page
    path('companion/',include('AppCompanion.urls'))         # companion page
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
