from django import forms
from .models import Post

class SelGrp(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('message',)

    # def clean_first_name(self):
    #     n = self.cleaned_data.get('first_name')
    #     if n.isdigit():
    #         raise forms.ValidationError('Cant be a number')
    #     return n