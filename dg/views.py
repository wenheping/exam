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
    context['what']='Welcome !     '

    return render(request,'dg.html',context)

def search_get(request):
    msg=''

    file_name=request.GET['ex_time']+request.GET['ex_grade']
    try:
      paper=DgBank.objects.get(dg_grade=request.GET['ex_grade'],dg_time=request.GET['ex_time'])
    except:
      pdf_name='notfound.pdf'
      msg='对不起，没找到试卷: '+file_name
    else:
      pdf_name=paper.dg_file+'.pdf'
      msg='找到了试卷：'+file_name

    pdf_file=os.path.join(PDF_DIR,pdf_name)

    if os.path.exists(pdf_file)==False:
       pdf_name='notfound.pdf'
       msg='对不起，试卷文件不存在: '+file_name

    context={}
    context['file_name']=pdf_name
    context['what']=msg

    return render(request,'dg.html',context)
