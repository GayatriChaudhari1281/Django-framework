from django import forms
from blog.models import Comments
class EmailSendForm(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    to=forms.EmailField()
    comments=forms.CharField(required=False,widget=forms.Textarea)
    #comment firld is not mandatorty
    #reuired=False means not mandatory


class CommentsForm(forms.ModelForm):
     class Meta:
         model=Comments
         fields=('name','email','body')
