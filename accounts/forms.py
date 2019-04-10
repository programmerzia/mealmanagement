# from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from accounts.models import User

class RegistrationForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username','email','password1','password2']

class UserForm(forms.ModelForm):
	

	class Meta:
		model = User
		fields = ['first_name','last_name','email','birthday','join_date','photo','address']