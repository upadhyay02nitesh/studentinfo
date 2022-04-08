from cProfile import label
from django.core import validators
from django import forms
from .models import User

class StudentRegistration(forms.ModelForm):
 class Meta:
  model = User
  fields = ['name','Fathername', 'email', 'password','image']
  widgets = {
   'name': forms.TextInput(attrs={'class':'form-control'}),
   'Fathername': forms.TextInput(attrs={'class':'form-control'}),
   'email': forms.EmailInput(attrs={'class':'form-control'}),
   'password': forms.PasswordInput(render_value=True, attrs={'class':'form-control'}),
   'image': forms.FileInput(),
  }
  labels = {
            'image': "Your Photo",
            'password':'Your Mobile No ',
            'Fathername':"Father Name"
        } 