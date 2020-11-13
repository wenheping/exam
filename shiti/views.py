from django.shortcuts import render
from django.http import HttpResponse
from django.http import FileResponse, Http404

def index(request):
    context={}
    context['file_name']='00000001.pdf'
    context['what']='Welcome !     '

    return render(request,'shiti.html',context)

