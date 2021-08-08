from django.contrib import admin
from demoapp.models import GrandParent,Parent,Child
# Register your models here.
class GrandParentAdmin(admin.ModelAdmin):
    list_display=['field1','field2']

class ParentAdmin(admin.ModelAdmin):
    list_display=['field1','field2','field3','field4']

class ChildAdmin(admin.ModelAdmin):
    list_display=['field1','field2','field3','field4','field5']

admin.site.register(GrandParent,GrandParentAdmin)
admin.site.register(Parent,ParentAdmin)
admin.site.register(Child,ChildAdmin)
