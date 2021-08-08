from django import forms
from django.core import validators
class StudentForm(forms.Form):
    def start_with_r(value):
        if value[0].lower()!='r':
            raise forms.ValidationError('Name should start r alphabet')
    def only_alpha(value):
        if value.isalpha()!=True:
            raise forms.ValidationError('Name should contains only alphabet')
    def gmail_verification(value):
        if value[len(value)-9:]!='gmail.com':
            print(value[len(value)-9:])
            raise forms.ValidationError('Mail should be gmail only')
    rollNo=forms.IntegerField()
    name=forms.CharField(validators=[start_with_r,only_alpha])
    address=forms.CharField()
    email=forms.EmailField(validators=[gmail_verification])
    feedback=forms.CharField(widget=forms.Textarea,validators=[validators.MaxLengthValidator(40),validators.MinLengthValidator(10)])
    password=forms.CharField(widget=forms.PasswordInput)
    Confirmpassword=forms.CharField(widget=forms.PasswordInput)


    '''def clean_name(self):
        nm=self.cleaned_data['name']
        if len(nm)<6:
            raise forms.ValidationError('The length of name field should be greater than the 6')
        return nm
    def clean_rollNo(self):
        rn=self.cleaned_data['rollNo']
        if len(str(rn))!=3:
            raise forms.ValidationError('Roll Number should be exactly 3 digits')
        return rn

    def clean(self):
        print("Total form validations")
        cleaned_data=super().clean()
        nm=cleaned_data['name']
        if len(nm)<6:
            raise forms.ValidationError('Name should compulsory contains atleast 6 character')

        rn=cleaned_data['rollNo']
        if len(str(rn))!=3:
            raise forms.ValidationError('Roll number contains exactly 3 digits')

        pswd=cleaned_data['password']
        cpswd=cleaned_data['Confirmpassword']
        if pswd!=cpswd:
            raise forms.ValidationError('Password mismatched!!')

        inputemail=cleaned_data['email']
        if inputemail[len(inputemail)-9:]!='gmail.com':
            raise forms.ValidationError('Mail should be gmail only')'''
"""every clean_fieldName() methods are instance method so compulsory we have to write self"""
