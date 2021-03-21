from django.db import models
from shiti.models import Shiti

import fitz

def get_filename(zhangjie):
    q=Shiti.objects.filter(w_zhishidian__contains=zhangjie)

    if q.count()>0 :
      return q[0].w_timu
    else:
      return "notfound"

def get_itemnum(zhangjie):
    q=Shiti.objects.filter(w_zhishidian__contains=zhangjie)
    num=q.count()
    return str(num)
