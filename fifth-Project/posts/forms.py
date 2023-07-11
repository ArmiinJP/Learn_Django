from django import forms

class PostForm(forms.Form):
    title = forms.CharField()
    text = forms.CharField(required=False, widget=forms.Textarea)
    is_enable = forms.BooleanField()
    publish_date = forms.DateField(required=False)