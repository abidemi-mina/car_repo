from django import forms
from django.contrib.auth.forms import PasswordChangeForm 
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core import validators


class ChangeWord(PasswordChangeForm):
	old_password = forms.CharField(label='Old Password', widget=forms.PasswordInput(attrs={ 'class':'form-control','placeholder':'Enter your old password'}))
	new_password1 = forms.CharField(label='New Password', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Enter new password'}))
	new_password2 = forms.CharField(label='Confirm New  Password', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Confirm new password'}))
	botfield = forms.CharField(required=False, widget=forms.HiddenInput(), validators=[validators.MaxLengthValidator(0)])
	class Meta():
		model = User
		fields = ( 'old_password','new_password1', 'new_password2')

	def save(self, commit=True):
	    user = super().save(commit=False)
	    user.old_password = self.cleaned_data['old_password']
	    user.new_password1 = self.cleaned_data['new_password1']
	    user.new_password2 = self.cleaned_data['new_password2']
	    

	    if commit:
	        user.save()
	        return user
