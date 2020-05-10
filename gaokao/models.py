from django.db import models

class GaokaoBank(models.Model):
  gk_id=models.IntegerField
  gk_subject=models.CharField(max_length=10)
  gk_type=models.CharField(max_length=20)
  gk_year=models.CharField(max_length=20)
  gk_name=models.CharField(max_length=100)
  gk_file=models.CharField(max_length=20)
  gk_file_ans=models.CharField(max_length=5,default='yes')
  gk_file_rev=models.CharField(max_length=5,default='no')
