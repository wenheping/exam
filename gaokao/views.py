from django.shortcuts import render
from django.http import HttpResponse
from django.http import FileResponse, Http404

import os

PROJ_DIR = os.path.dirname(os.path.dirname(__file__))
PDF_DIR=os.path.join(PROJ_DIR,'wenfiles/pdf/dg/')

def index(request):
    pdf_name='start_gk.pdf'

    context={}
    context['file_name']=pdf_name
    context['what']=PROJ_DIR

    return render(request,'gk.html',context)
