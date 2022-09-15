from django.contrib import admin
from myapp.models import BoardTab

# Register your models here.
class BoardAdmin(admin.ModelAdmin):
    list_display = ('id','name','mail','title','cont','bdate','readcnt','gnum','onum','nested')
    
admin.site.register(BoardTab, BoardAdmin)    