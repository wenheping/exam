from django.db import models

class ExamBank(models.Model):
  exam_id=models.IntegerField
  exam_type=models.CharField(max_length=10)
  exam_loc=models.CharField(max_length=10)
  exam_time=models.CharField(max_length=10)
  exam_grade=models.CharField(max_length=20)
  exam_name=models.CharField(max_length=100)
  exam_file=models.CharField(max_length=10)
