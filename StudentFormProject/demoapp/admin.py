from django.contrib import admin
from demoapp.models import Student


# Register your models here.
class StudentForm_admin(admin.ModelAdmin):
    list_display=['name','rollNo','address','email','feedback']

admin.site.register(Student,StudentForm_admin)
