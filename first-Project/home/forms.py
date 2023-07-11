from django import forms
from home.models import Animal


class CreateAnimalForm(forms.Form):
    title = forms.CharField()
    body = forms.CharField()
    created = forms.DateTimeField()
    
class UpdateAnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = "__all__"

