from django.shortcuts import render
from django.http import HttpResponse
from django.http import FileResponse, Http404

import os

from .models import DgBank

PROJ_DIR = os.path.dirname(os.path.dirname(__file__))
PDF_DIR=os.path.join(PROJ_DIR,'wenfiles/pdf/dg/')

def index(request):
    pdf_name='start.pdf'

    context={}
    context['file_name']=pdf_name
    context['what']='File existis !'+pdf_name

    return render(request,'dg.html',context)

def search_get(request):
    file_name=request.GET['ex_grade']+request.GET['ex_year']
    try:
      paper=DgBank.objects.get(dg_grade=request.GET['ex_grade'])
    except:
      pdf_name='notfound.pdf'
      tmp='did not found: '+file_name
    else:
      pdf_name=paper.dg_file+'.pdf'
      tmp='found it !'+file_name

    pdf_file=os.path.join(PDF_DIR,pdf_name)

    if os.path.exists(pdf_file)==False:
       pdf_name='notfound.pdf'
       tmp='did not found: '+file_name

    context={}
    context['file_name']=pdf_name
    context['what']=tmp

    return render(request,'dg.html',context)
