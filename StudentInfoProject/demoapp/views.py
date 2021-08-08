from django.shortcuts import render
from demoapp.models import Student
# Create your views here.
def student_info_view(request):
    student=Student.objects.all()#django-ORM
    return render(request,'demoapp/student.html',{'stud':student})
