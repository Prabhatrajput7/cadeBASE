from django import forms
from app.models import Imgg


class FFM(forms.ModelForm):
    class Meta:
        model = Imgg
        fields = ['img']

class FF(forms.Form):
    img = forms.ImageField()


"""
widget=forms.ClearableFileInput(attrs={'name':'imagee'})
widget=forms.TextInput(attrs={'name':'imagee'}))
 widgets = {
            'img': forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
        }
"""