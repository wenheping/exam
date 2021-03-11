from django.db import models

# Create your models here.

class Shiti(models.Model):
    w_id = models.IntegerField(default=0)
    w_timu = models.CharField(max_length=8)
    w_daan = models.TextField()
    w_jiexi_lei = models.CharField(max_length=8)
    w_jiexi = models.TextField(null=True)
    w_shijuan_lei = models.CharField(max_length=20)
    w_shiti_lei = models.CharField(max_length=10)
    w_quyu = models.CharField(max_length=20)
    w_nian = models.IntegerField(default=2020)
    w_nandu = models.IntegerField(default=3)
    w_zhiliang = models.IntegerField(default=3)
    w_zhishidian = models.CharField(max_length=100,default='')
    w_guanjianci = models.CharField(max_length=30)
