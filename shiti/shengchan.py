from django.db import models
from shiti.models import Shiti

def get_filename(zhangjie):
    q=Shiti.objects.filter(w_zhishidian__startswith=zhangjie)
    print(q.count())
    if q.count()>0 :
      return "00000003"
    else:
      return "00000008"
