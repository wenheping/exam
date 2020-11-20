from django.db import models

# Create your models here.

class Shiti(models.Model):
    w_id = models.IntegerField(default=0)
    w_timu = models.CharField(max_length=20)
    w_daan = models.CharField(max_length=20)
    w_jiexi_lei = models.CharField(max_length=20)
    w_jiexi = models.CharField(max_length=10)
    w_shijuan_lei = models.CharField(max_length=20)
    w_shiti_lei = models.CharField(max_length=20)
    w_quyu = models.CharField(max_length=20)
    w_nian = models.CharField(max_length=10)
    w_nandu = models.CharField(max_length=10)
    w_zhiliang = models.CharField(max_length=10)
    w_zhishidian = models.CharField(max_length=10)
    w_guanjianci = models.CharField(max_length=10)
    
