from django.contrib import admin

# Register your models here.

from .models import Shiti

class ShitiAdmin(admin.ModelAdmin):
  list_display=('w_id','w_shijuan_lei','w_shiti_lei','w_nian','w_zhishidian')
  list_display_links=('w_id','w_shijuan_lei','w_shiti_lei','w_nian','w_zhishidian')
  list_per_page=20

admin.site.register(Shiti,ShitiAdmin)
