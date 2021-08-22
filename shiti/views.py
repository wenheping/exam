from django.shortcuts import render
from django.http import HttpResponse
from django.http import FileResponse, Http404
from django.views.decorators.http import require_POST
from django.http import JsonResponse

from . import shengchan

import random,json

def index(request):
    context={}
    context['file_name']='welcome.pdf'
    context['what']='Welcome !     '
    return render(request,'shiti.html',context)

@require_POST
def api(request):
    file_name=''

    code = request.POST.get('pdata')
    test1=request.POST.get('t1data')
    test2=request.POST.get('t2data')
    test3=request.POST.get('t3data')

    if (code.find('mis')>=0):
      return JsonResponse(data={'output':'click_next'})
    else:
      file_name=shengchan.get_filename(code,test1,test2,test3)
      item_num=shengchan.get_itemnum(code)
      return JsonResponse(data={'output':file_name,'timushu':item_num})
