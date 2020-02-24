from django.shortcuts import render
from django.http import HttpResponse
from django.http import FileResponse, Http404

def index(request):
    return HttpResponse("Hello, Here is paper manage system ")

def display(request,paper_id):
    context={}
    context['file_name']="paper"+str(paper_id)
    context['what']='I am a template, my name is display!'
    return render(request,'home.html',context)
