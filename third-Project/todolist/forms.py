from django import forms
from todolist import models


class CreateTodoForm(forms.ModelForm):
    """Form definition for CreateTodo."""

    class Meta:
        """Meta definition for CreateTodoform."""
        model = models.Todo
        fields = '__all__'

class UpdateTodoForm(forms.ModelForm):
    class Meta:
        model = models.Todo
        fields = '__all__'
        
    # name = forms.CharField()
    # category = forms.CharField()
    # description = forms.CharField(required=False)
    # deadline = forms.TimeField(required=False)