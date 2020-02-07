from django.shortcuts import render
from django.http import HttpResponse
from django.http import FileResponse, Http404

def index(request):
    return HttpResponse("Hello, Here is paper manage system ")

def display(request):
    context={}
    return render(request,'tmp.html',context)

def display2(request):
    context={}
    context['what']='I am a template, my name is what !'
    return render(request,'home.html',context)
