from django.urls import path,re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:dg_id>/', views.display, name='display'),
    re_path(r'^search$', views.search_get, name='search_get'),
]
