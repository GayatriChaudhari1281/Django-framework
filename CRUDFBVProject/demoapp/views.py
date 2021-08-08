from django.shortcuts import render,redirect
from demoapp.forms import EmployeeForm
from demoapp.models import Employee
# Create your views here.
def read_view(request):
    employee=Employee.objects.all()
    return render(request,'demoapp/index.html',{'emp':employee})

def insert_view(request):
    formObj=EmployeeForm()
    if request.method=='POST':
        formObj=EmployeeForm(request.POST)
        if formObj.is_valid():
            formObj.save()
        return redirect('/read')
    return render(request,'demoapp/insert.html',{'fobj':formObj})


def delete_view(request,id):
    employee=Employee.objects.get(id=id)
    employee.delete()
    return redirect('/read')

def update_view(request,id):
    employee=Employee.objects.get(id=id)
    if request.method=='POST':
        formObj=EmployeeForm(request.POST,instance=employee)
        if formObj.is_valid():
            formObj.save()
        return redirect('/read')
    return render(request,'demoapp/update.html',{'emp':employee})
