
from django.contrib import admin
from django.urls import path , include
from django.views.static import serve
from django.conf.urls.static import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('app.urls'))
    urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("Home.urls")),
]
]
