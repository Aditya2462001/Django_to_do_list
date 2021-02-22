from django.contrib import admin

from .models import Data
# Register your models here.

admin.site.register(Data)


admin.site.site_header = 'Django TO DO LIST'
admin.site.index_title = 'To Do List Admin' 
admin.site.site_title = 'To Do List'