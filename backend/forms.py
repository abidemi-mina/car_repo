from django import forms
from django.contrib.auth.forms import PasswordChangeForm 
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core import validators


class ChangePas(PasswordChangeForm):
	oldpasword = forms.CharField(label='OLD Password', widget=forms.PasswordInput(attrs={ 'class':'form-control','placeholder':'Enter your old password'}))
	password1 = forms.CharField(label='New Password', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Enter new password'}))
	password2 = forms.CharField(label='Confirm New  Password', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Confirm new password'}))
	botfield = forms.CharField(required=False, widget=forms.HiddenInput(), validators=[validators.MaxLengthValidator(0)])
	class Meta():
		model = User
		fields = ( 'oldpasword','password1', 'password2')

	def save(self, commit=True):
	    user = super().save(commit=False)
	    user.oldpasword = self.cleaned_data['oldpasword']
	    user.password1 = self.cleaned_data['password1']
	    user.password2 = self.cleaned_data['password2']
	    

	    if commit:
	        user.save()
	        return user
