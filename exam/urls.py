from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dg/',include('dg.urls')),
    path('ss/',include('ss.urls')),
    path('',include('shiti.urls')),
]
