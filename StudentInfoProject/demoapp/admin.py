from django.contrib import admin
from demoapp.models import Student
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display=['rollNo','name','marks','address','dob','email','mobno']

admin.site.register(Student,StudentAdmin)
#username-gayatri1281
#password-Gaya@128
