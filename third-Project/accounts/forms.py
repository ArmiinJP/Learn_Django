from django import forms

class LoginUserForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

class RegisterUserForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()

