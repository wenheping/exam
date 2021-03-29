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
         doc=fitz.open(pdf_path+q[i].w_timu+".pdf") # open origin pdf item
         tmp.insert_pdf(doc)
         block_lenth=len(tmp[0].getTextBlocks())
         r1=tmp[0].getTextBlocks()[block_lenth-1][0]
         r2=tmp[0].getTextBlocks()[block_lenth-1][3] # get the bottom of the text

         pos1=fitz.Rect(80,50,400,500)
         pos2=fitz.Rect(105,50,400,500)
         tmp[i].insert_textbox(pos1,"2020",color=(0,0,1))
         tmp[i].insert_textbox(pos2,q[i].w_shijuan_lei,fontname="china-ss",color=(0,0,1))
         # add the header to tell which year, which district

         pos3=fitz.Rect(r1,r2+20,595,842)
         tmp[i].insert_textbox(pos3,"答案：",fontname="china-ss",color=(1,0,0))
         # add the bottom to tell the key and the explation.

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
