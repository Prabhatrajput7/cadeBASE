from django import forms

class FileFieldForm(forms.Form):
    name = forms.CharField()
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))