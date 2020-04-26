from django.db import models

class DgBank(models.Model):
  dg_id=models.IntegerField
  dg_subject=models.CharField(max_length=10)
  dg_grade=models.CharField(max_length=20)
  dg_time=models.CharField(max_length=20)
  dg_name=models.CharField(max_length=100)
  dg_file=models.CharField(max_length=10)
  dg_file_ans=models.CharField(max_length=5,default='yes')
  dg_file_rev=models.CharField(max_length=5,default='no')
