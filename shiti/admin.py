from django.contrib import admin

# Register your models here.

from .models import Content, Attrib
admin.site.register(Content)
admin.site.register(Attrib)
