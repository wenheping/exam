from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pdf_id>', views.pdf2, name='pdf2'),
    path('display2', views.display2, name='display2'),
    path('pdf', views.pdf, name='pdf'),
]
