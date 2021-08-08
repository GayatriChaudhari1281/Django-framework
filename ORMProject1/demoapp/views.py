from django.shortcuts import render
from demoapp.models import Employee
# Create your views here.
def display_view(request):
    #employee=Employee.objects.all()
    employee=Employee.objects.get_empsalrange(180000,240000)
    my_dict={'emp':employee}
    return render(request,'demoapp/index.html',my_dict)
