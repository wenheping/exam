from django.shortcuts import render
from django.http import HttpResponse
from django.http import FileResponse, Http404

def index(request):
    return HttpResponse("Hello, Here is paper manage system ")

def display(request, paper_id):
    res= "Hi, I am paper%s "
    return HttpResponse(res % paper_id)

def display2(request):
    context={}
    context['what']='I am a template, my name is what !'
    return render(request,'home.html',context)

def pdf(request):
    try:
        return FileResponse(open('wenfiles/pdf/paper1.pdf', 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()

def pdf2(request, pdf_id):
    try:
        file_name='wenfiles/pdf/paper'+str(pdf_id)+'.pdf'
        return FileResponse(open(file_name, 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()
