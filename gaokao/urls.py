from django.urls import path,re_path
from django.urls import path
from . import views

urlpatterns=[
  path('',views.index, name='index'),
  re_path(r'^search$', views.search_get, name='search_get'),
]
