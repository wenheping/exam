from django.http import HttpResponse


def index(request):
    return HttpResponse("Now start the real work !")

