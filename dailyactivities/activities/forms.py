from django import forms
from django.contrib.auth.models import User
from django.core.validators import validate_email
from .models import Activity_model

class UserForm(forms.ModelForm):
	username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter username'}),required=True,max_length=50)
	email=forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter email'}),required=True,max_length=50)
	first_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter first name'}),required=True,max_length=30)
	last_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter last name'}),required=True,max_length=30)
	password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter password'}),required=True,max_length=30)
	confirm_password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm password'}),required=True,max_length=30)
	
	class Meta():
		model=User
		fields=['username','email','first_name','last_name','password']

	def clean_username(self):
		user=self.cleaned_data['username']
		try:
			match=User.objects.get(username=user)
		except:
			return self.cleaned_data['username']
		raise forms.ValidationError("Username already exist...")

	def clean_email(self):
		get_email=self.cleaned_data['email']
		try:
			match=validate_email(get_email)
		except:
			raise forms.ValidationError("Email is not in correct format...")
		return self.cleaned_data['email']	

	def clean_confirm_password(self):
		pass1=self.cleaned_data['password']
		con_pass=self.cleaned_data['confirm_password']
		max_length=5
		if pass1 and con_pass:
			if pass1 != con_pass:
				raise forms.ValidationError("password confirm password not matched")
			else:
				if len(pass1)<max_length:
					raise forms.ValidationError("Password should have atleast %d characters" %max_length)
				if pass1.isdigit():
					raise forms.ValidationError("password should not all numeric")

class ActivityForm(forms.ModelForm):
	Activity_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Activity Name'}))
	Activity=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Activity'}))
	
	class Meta():
		model=Activity_model
		fields=['Activity_name','Activity','file']
