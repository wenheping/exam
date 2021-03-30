from django.db import models
from shiti.models import Shiti

import fitz,uuid

pdf_path="/root/wen/exam/wenfiles/shiti/2020/"

def w_uuid(string_length=10):
    random = str(uuid.uuid4())
    random = random.replace("-","")
    return random[0:string_length]

def w_bottom(page):
    # this function return the bottom position to add some text
    b_num=len(page.getTextBlocks())
    my_bottom=page.getTextBlocks()[0][3]
    if b_num>1 :
      for i in range(1,b_num,1):
        if page.getTextBlocks()[i][3]>my_bottom :
           my_bottom=page.getTextBlocks()[i][3]
    return my_bottom

def get_filename(zhangjie):
    q=Shiti.objects.filter(w_zhishidian__contains=zhangjie)
    item_num=q.count()

    if item_num>0 :
      tmp=fitz.open()
      for i in range(item_num):
         doc=fitz.open(pdf_path+q[i].w_timu+".pdf") # open origin pdf item
         tmp.insert_pdf(doc)
#         block_lenth=len(doc[0].getTextBlocks())
#         r1=doc[0].getTextBlocks()[block_lenth-1][0]
#         r2=doc[0].getTextBlocks()[block_lenth-1][3] # get the bottom of the text
         r2=w_bottom(doc[0])

         pos1=fitz.Rect(80,50,400,500)
         pos2=fitz.Rect(105,50,400,500)
         tmp[i].insert_textbox(pos1,"2020",color=(0,0,1))
         tmp[i].insert_textbox(pos2,"年"+q[i].w_shijuan_lei,fontname="china-ss",color=(0,0,1))
         # add the header to tell which year, which district

         pos3=fitz.Rect(80,r2+30,595,842)
         tmp[i].insert_textbox(pos3,"答案：",fontname="china-ss",color=(1,0,0))
         pos3=fitz.Rect(90,r2+45,595,842)
         tmp[i].insert_textbox(pos3,q[i].w_daan,fontname="china-ss",color=(1,0,0))
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
