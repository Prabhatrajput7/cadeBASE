from django import forms
from django.forms import ModelForm
from app.models import Review

class ReviewForm(forms.Form):
    first_name = forms.CharField(label='First Name',max_length=10,widget=forms.TextInput(attrs={'class':'revew','placeholder': 'Fname'}), error_messages ={'max_length':'Not more than 10'})
    last_name = forms.CharField(label="Last Name",max_length=10)
    email = forms.EmailField(label='Email')
    review = forms.CharField(label='Review',widget=forms.Textarea(attrs={'class':'review'}))

    #attrs={'class':'review'}) these are the class of html to sytle the element this 
    # should be under widget

    def clean_first_name(self):
        n = self.cleaned_data.get('first_name')
        if n.isdigit():
            raise forms.ValidationError('Cant be a number')
        return n

    def clean_last_name(self):
        n = self.cleaned_data.get('last_name')
        if n.isdigit():
            raise forms.ValidationError('Cant be a number')
        return n

class ReviewFormM(ModelForm):
    class Meta:
        model = Review 
        # fields = ['first_name','last_name','stars']
        fields = "__all__"

        labels = {
            'first_name':"F Name",
            'last_name':"L Name",
            'stars':'Rating'
        }
        # https://docs.djangoproject.com/en/4.0/ref/forms/fields/#built-in-field-classes

        error_messages = {
            'stars':{
                'min_value':"Yo! Minimum value must be 1",
                'max_value':"Yo! Max value is 5"
            }
        }    

        widgets = {
            'first_name': forms.TextInput(attrs={'class':'revew','placeholder': 'FFname'}),
        }

    def clean_first_name(self):
        n = self.cleaned_data.get('first_name')
        if n.isdigit():
            raise forms.ValidationError('Cant be a number')
        return n



"""
widgets = {
            'report_number': forms.CharField(attrs={'class': 'form-control'}),
            'request_number': forms.CharField(attrs={'class': 'form-control'}),
            'request_reason': forms.CharField(attrs={'class': 'form-control'}),
            'actions_taken': forms.Textarea(attrs={'class': 'form-control'}),
        }
"""        

"""
from django.forms import ModelForm
from django import forms
from formValidationApp.models import *

# define the class of a form
class PostForm(ModelForm):
	class Meta:
		# write the name of models for which the form is made
		model = Post	

		# Custom fields
		fields =["username", "gender", "text"]

	# this function will be used for the validation the entire form 
	def clean(self):

		# data from the form is fetched using super function
		super(PostForm, self).clean()
		
		# extract the username and text field from the data
		username = self.cleaned_data.get('username')
		text = self.cleaned_data.get('text')

		# conditions to be met for the username length
		if len(username) < 5:
			self._errors['username'] = self.error_class([
				'Minimum 5 characters required'])
		if len(text) <10:
			self._errors['text'] = self.error_class([
				'Post Should Contain a minimum of 10 characters'])

		# return any errors if found
		return self.cleaned_data

        #or

        form.Form

        email = forms.EmailField()
        verify_email = forms.EmailField(label='Enter your email again:')
        #inside class
        def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']

        if email != vmail:
            raise forms.ValidationError("MAKE SURE EMAILS MATCH!")

"""

# we do this to protect against bot
# when a bot scrape website input = hidden is not present on html but present in code
# when user submit it with value= 'bot' we will catch it via len fx
"""
botcatcher = forms.CharField(required = False, widget = forms.HiddenInput)
#inside class
def clean_botcatcher(self):
    botcatcher = self.cleaned_data['botcatcher']
    if len(botcatcher)>1:
        raise forms.Validation('Fuckin Bot')
    return botcatcher

or build in validators 
botcatcher = forms.CharField(required = False, widget = forms.HiddenInput, validators=[validatos.MaxlengthValidator(0)])    
"""


#Build in custome Validator

"""
django.core import validator

forms.Form 
name = forms.CharField()
#outside the class

def checkforz(value):
    if value[0].lower()!='z':
        raise forms.validateerror('need to start with z')

name = forms.CharField(validators=[validatos.checkforz])
"""