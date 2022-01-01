from django.urls import re_path
#from django.conf.urls import url

from . import views

urlpatterns = [
    re_path('^$', views.index, name='index'),
    re_path('^api/$', views.api, name='api')
]
