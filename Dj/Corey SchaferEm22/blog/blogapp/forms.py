from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):

    content = forms.CharField(max_length=100, label="Add a comment")
    
    class Meta:
        model = Comment
        fields = ('content',)

        # widgets = {
        #     'content': Textarea(attrs={'cols': 80, 'rows': 20}),
        # }

# class ReplyForm(forms.ModelForm):
#     class Meta:
#         model = Reply
#         fields = ('reply_body',)

        # widgets = {
        #     'reply_body': forms.Textarea(attrs={'class':'form-control', 'rows':2, 'cols':10}),
        # }    
