from django import forms
from django.contrib.auth.models import User

class RegisterUserForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField()
    last_name = forms.CharField()

class LoginUserForm(forms.Form):
    username = forms.CharField()    
    password = forms.CharField()

# class RegisterUserForm(forms.ModelForm):
#     class Meta:
#         model User