from django.shortcuts import render
from django.http import HttpResponse
from django.http import FileResponse, Http404

import os

pdf_dir='/root/wen/exam/wenfiles/pdf'

def search_get(request):
    if 'q' in request.GET:
      pdf_name='paper'+request.GET['q']+'.pdf'
      pdf_file=os.path.join(pdf_dir,pdf_name)

      if os.path.exists(pdf_file)==False:
         pdf_name='notfound.pdf'

      context={}
      context['file_name']=pdf_name
      context['what']='File existis !'+pdf_name

    return render(request,'home.html',context)
