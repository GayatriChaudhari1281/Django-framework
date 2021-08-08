from django.contrib import admin
from demoapp.models import Employee
# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display=['eno','ename','esal','eaddress']

admin.site.register(Employee,EmployeeAdmin)
#username:gayatri
#password- Gaya@128
#gayatri.chaudhari@gmail.com
