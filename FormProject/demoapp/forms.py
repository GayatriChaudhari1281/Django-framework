from django import forms

class EmployeeForm(forms.Form):
    eno=forms.IntegerField()
    ename=forms.CharField()
    esal=forms.FloatField()
    eaddress=forms.CharField()
