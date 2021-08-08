from django.shortcuts import render
from . import forms
# Create your views here.

'''def success_view(request):
    return render(request,'demoapp/success.html')'''
def feedback_view(request):
    if request.method=='GET':
        formObj=forms.StudentForm()
    #return render(request,'demoapp/register.html',{'fobj':formObj})
    if request.method=='POST':
        formObj=forms.StudentForm(request.POST)
        if formObj.is_valid():
            print("Form Validate Successfully!!")
            print("Roll Number:",formObj.cleaned_data['rollNo'])
            print("Name:",formObj.cleaned_data['name'])
            print("Email Id:",formObj.cleaned_data['email'])
            print("feedback:",formObj.cleaned_data['feedback'])
    return render(request,'demoapp/register.html',{'fobj':formObj})
    #return success_view(request)
