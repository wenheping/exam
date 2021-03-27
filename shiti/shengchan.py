from django.db import models
from shiti.models import Shiti

import fitz,uuid

pdf_path="/root/wen/exam/wenfiles/shiti/2020/"

def w_uuid(string_length=10):
    random = str(uuid.uuid4())
    random = random.replace("-","")
    return random[0:string_length]

def get_filename(zhangjie):
    q=Shiti.objects.filter(w_zhishidian__contains=zhangjie)
    item_num=q.count()

    if item_num>0 :
      tmp=fitz.open()
      for i in range(item_num):
         doc=fitz.open(pdf_path+q[i].w_timu+".pdf")
         tmp.insert_pdf(doc)
         doc.close()
      file_name=w_uuid()
      tmp.save(pdf_path+file_name+".pdf")
      return file_name
    else:
      return "notfound"

def get_itemnum(zhangjie):
    q=Shiti.objects.filter(w_zhishidian__contains=zhangjie)
    num=q.count()
    return str(num)
