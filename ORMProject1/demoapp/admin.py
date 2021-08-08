from django.contrib import admin
from demoapp.models import Employee,ProxyEmployee,ProxyEmployee2
# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['id','eno','ename','esal','eaddress']


class ProxyEmployeeAdmin(admin.ModelAdmin):
    list_display=['id','eno','ename','esal','eaddress']

class ProxyEmployee2Admin(admin.ModelAdmin):
    list_display=['id','eno','ename','esal','eaddress']

admin.site.register(Employee,EmployeeAdmin)
admin.site.register(ProxyEmployee,ProxyEmployeeAdmin)
admin.site.register(ProxyEmployee2,ProxyEmployee2Admin)
