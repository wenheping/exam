from django.conf import settings
from django.http import HttpResponse
from django.conf.urls import url

from django.views.decorators.http import require_POST
from django.http import JsonResponse

import random

setting = {
    'DEBUG':True,
    'ROOT_URLCONF':__name__
}

settings.configure(**setting)

def home(request):
    with open('index.html','rb') as f:
        html = f.read()
    return HttpResponse(html)

@require_POST
def api(request):
    code = request.POST.get('code')
    output = random.randint(0,100)
    return JsonResponse(data={'output':output})

urlpatterns = [url('^api/$',api,name='api'),
               url('^$',home,name='home')]

if __name__ == '__main__':
    import sys
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
