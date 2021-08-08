from django.contrib import admin
from demoapp.models import Student
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display=['rollNo','name','marks']

admin.site.register(Student,StudentAdmin)
#username:gayatri
#password- Gaya@128
#gayatri.chaudhari@gmail.com
