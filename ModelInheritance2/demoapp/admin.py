from django.contrib import admin
from demoapp.models import PersonalData,Student,Teacher
# Register your models here.
class PersonalDataAdmin(admin.ModelAdmin):
    list_display=['name','email','address']

class StudentAdmin(admin.ModelAdmin):
    list_display=['name','email','address','rollno','marks']

class TeacherAdmin(admin.ModelAdmin):
    list_display=['name','email','address','subject','salary']

admin.site.register(PersonalData,PersonalDataAdmin)
admin.site.register(Student,StudentAdmin)
admin.site.register(Teacher,TeacherAdmin)
