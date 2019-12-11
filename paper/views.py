from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, Here is paper manage system ")

def display(request, paper_id):
    res= "Hi, I am paper%s "
    return HttpResponse(res % paper_id)
