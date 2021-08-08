from django.shortcuts import render
from demoapp.models import Employee
# Create your views here.
def employee_info_view(request):
    employee=Employee.objects.all()#django-ORM
    return render(request,'demoapp/emp.html',{'emp':employee})
