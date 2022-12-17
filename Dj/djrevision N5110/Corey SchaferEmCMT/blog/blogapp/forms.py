from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):

    content = forms.CharField(max_length=100, label="", widget=forms.Textarea(attrs={'placeholder':'test goes here!!!','cols': 100, 'rows': 2}))
    
    class Meta:
        model = Comment
        fields = ('content',)

        # widgets = {
        #     'content': forms.Textarea(attrs={'cols': 8, 'rows': 2,'placeholder':'test goes here'}),
        # }
class CommentForm2(forms.ModelForm):

    content = forms.CharField(max_length=100, label="", widget=forms.Textarea(attrs={'placeholder':'test goes here!!!','cols': 100, 'rows': 2}))
    
    class Meta:
        model = Comment
        fields = ('content',)
# class ReplyForm(forms.ModelForm):
#     class Meta:
#         model = Reply
#         fields = ('reply_body',)

        # widgets = {
        #     'reply_body': forms.Textarea(attrs={'class':'form-control', 'rows':2, 'cols':10}),
        # }    
