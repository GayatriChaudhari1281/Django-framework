from django import forms
from demoapp.models import Student

class StudentForm(forms.ModelForm):
    #fields declaration
    #validation here 
    class Meta:
        model=Student
        fields='__all__'
