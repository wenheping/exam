from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('display', views.display, name='display'),
    path('display2', views.display2, name='display2'),
]
