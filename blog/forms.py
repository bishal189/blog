from django import forms
from .models import  comment
class SpecificForm(forms.ModelForm):
    class Meta:
        model = comment
        fields = "__all__"
        exclude=('post',)
  

    
