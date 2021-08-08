from django import forms
from demoapp.models import Icecream

class IcecreamForm(forms.ModelForm):
    class Meta:
        model=Icecream
        fields='__all__'
