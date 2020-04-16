from django.urls import path,re_path

from . import views, forms

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:paper_id>/', views.display, name='display'),
    re_path(r'^index$', views.index, name='index'),
    re_path(r'^search$', forms.search_get, name='search_get'),
]
