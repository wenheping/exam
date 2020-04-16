from django.db import models

class ExamBank(models.Model):
  ex_id=models.IntegerField
  ex_type=models.CharField(max_length=10)
  ex_loc=models.CharField(max_length=10)
  ex_time=models.CharField(max_length=20)
  ex_grade=models.CharField(max_length=20)
  ex_name=models.CharField(max_length=100)
  ex_file=models.CharField(max_length=10)
  ex_file_ans=models.CharField(max_length=5,default='yes')
  ex_file_rev=models.CharField(max_length=5,default='no')
