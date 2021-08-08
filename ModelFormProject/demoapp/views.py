from django.shortcuts import render
from demoapp import forms
# Create your views here.
def student_view(request):
    formObj=forms.StudentForm()#object creation
    if request.method=='POST':
        formObj=forms.StudentForm(request.POST)#object creation
        if formObj.is_valid():
            formObj.save(commit=True)#responsible to add form data into db table
            print('Form Data insertedd succesfully in DB table!!')
    return render(request,'demoapp/index.html',{"fobj":formObj})
