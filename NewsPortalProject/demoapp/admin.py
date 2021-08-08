from django.contrib import admin

# Register your models here.
from demoapp.models import FilterModel

class FilterModelAdmin(admin.ModelAdmin):
    list_display=['id','name','subject','dept','date']

admin.site.register(FilterModel,FilterModelAdmin)
