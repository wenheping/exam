from django.shortcuts import render
from django.http import HttpResponse
from django.http import FileResponse, Http404
from django.views.decorators.http import require_POST
from django.http import JsonResponse

import random

def index(request):
    context={}
    context['file_name']='00000001.pdf'
    context['what']='Welcome !     '
    return render(request,'shiti.html',context)

@require_POST
def api(request):
    code = request.POST.get('pdata')
    output = random.randint(0,100)
    return JsonResponse(data={'output':output})
