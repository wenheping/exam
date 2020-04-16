from django.shortcuts import render
from django.http import HttpResponse
from django.http import FileResponse, Http404

import os

pdf_dir='/root/wen/exam/wenfiles/pdf'

def index(request):
    pdf_name='start.pdf'

    context={}
    context['file_name']=pdf_name
    context['what']='File existis,please update !    '+pdf_name

    return render(request,'home.html',context)

def display(request,paper_id):
    pdf_name='paper'+str(paper_id)+'.pdf'
    pdf_file=os.path.join(pdf_dir,pdf_name)

    context={}

    if os.path.exists(pdf_file)==True:
        context['file_name']=pdf_name
        context['what']='File existis !'+pdf_file
    else:
        context['file_name']='notfound.pdf'
        context['what']='File does not exist !'+pdf_file

    return render(request,'home.html',context)
