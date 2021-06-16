from django import forms
from django.contrib.auth.forms import PasswordChangeForm 
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core import validators
from Cars.models import *
from django.shortcuts import reverse



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
class BrandForm(forms.ModelForm):
	name = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))

	class Meta():
		model = Brands
		fields = '__all__'


class CarTypeForm(forms.ModelForm):
	names = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),)
	class Meta():
		model = Car_Type
		fields =('names',)



class DealerForm(forms.ModelForm):
    user_id = forms.ModelChoiceField(
		queryset=User.objects.all(), 
		widget=forms.Select(attrs={'class':'form-control'}), 
		empty_label='Select a User'
		)
    phone = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    website = forms.URLField(widget=forms.URLInput(attrs={'class':'form-control'}))
    profile = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class':'form-control'}))
    biography = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
    address = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))





class LocationForm(forms.ModelForm):
	name =forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

	class Meta():
		model = Location
		fields = ('name',)



	
class CarForm(forms.ModelForm):
	RENT = 'Rent'
	SALE = 'Sale'
	CHOOSE = ''
	OFFER_TYPE = [
		(RENT, 'Rent'),
		(SALE, 'Sale'),
		(CHOOSE, 'Choose An Offer Type'),
	]

	USED = 'Foreign Used'
	NEW = 'New'
	CHOOSE = ""
	CONDITION = [
		(USED , 'Foreign Used'),
		(NEW , 'New'),
		(CHOOSE, 'What is the car status')
	]

	AUTOMATIC = 'Automatic'
	MANUAL = 'Manual'
	CHOOSE = ""
	SELECT = [
		(AUTOMATIC, 'Automatic'),
		(MANUAL, 'Manual'),
		(CHOOSE, "Select Transmission")
	]


	
	make = forms.ModelChoiceField(
		queryset= Brands.objects.all(),
		widget=forms.Select(attrs={'class':'form-control'}),
		empty_label= 'Select maker'
	)
	vehicle_type= forms.ModelChoiceField(
		queryset=Car_Type.objects.all(),
		widget=forms.Select(attrs={'class':'form-control'}),
		empty_label='Select vehicle type '
	)
	car_model = forms.CharField(widget=forms.TextInput())
	location_id = forms.ModelChoiceField(
		queryset=Location.objects.all(),
		widget= forms.Select(attrs={'class':'form-control'}),
		empty_label= 'Select your location'
	)
	offer_type = forms.ChoiceField(widget=forms.Select(choices=OFFER_TYPE), )
	milleage = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	status = forms.ChoiceField(widget=forms.Select(choices=CONDITION, attrs={'class':'form-control'}))
	transmission = forms.ChoiceField(widget=forms.Select(choices=SELECT, attrs={'class':'form-control'}),)
	color = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	car_description =forms.ChoiceField(widget= forms.Textarea(attrs={'class':'form-control'}))
	fuel = forms.ChoiceField(widget=forms.TextInput(attrs={'class':'form-control'}))
	offer_type = forms.ChoiceField(widget=forms.Select(choices=OFFER_TYPE, attrs={'class':'form-control'}))
	transmission = forms.ChoiceField(widget=forms.Select(choices=SELECT,attrs={'class':'form-control'}))
	car_image = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class':'form-control'}))
	car_image1 = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class':'form-control'}))
	car_image2 = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class':'form-control'}))
	car_image3 = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class':'form-control'}))
	maintenance = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
	prize = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'form-control'}))
	old_prize = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'form-control'}))
	first_registration = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
	approve = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class':'form-control'}))
	manufacturing_date = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control'}))

	class Meta():
		model = Cars
		exclude = ('created', 'slug')




class BlogForm(forms.ModelForm):
	POLITICS = 'Politics'
	SPORTS = 'Sports'
	AUTOMOBILE = 'Automobile'
	TECHNOLOGY = 'Technology'
	ENTERTAINMENT = 'Entertainment'
	BUSINESS = "Business"
	HEALTH = 'Health'
	CHOOSE = ""
	SELECT = [
		(POLITICS, 'Politics'),
		(SPORTS, 'Sports'),
		(AUTOMOBILE, 'Automobile' ),
		(TECHNOLOGY, 'Technology'),
		(ENTERTAINMENT, 'Entertainment'),
		(BUSINESS, 'Business'),
		(HEALTH, 'Health'),
		(CHOOSE, 'Select category')

	]
   
	title = forms.CharField(widget= forms.Textarea(attrs={'class':'form-control'}))
	author = forms.ModelChoiceField(
	queryset= User.objects.all(), 
	widget= forms.Select(attrs={'class':'form-control'}), 
	empty_label='Select Author'
	)
	category = forms.ChoiceField(widget=forms.Select(choices=SELECT,attrs={'class':'form-control'}))
	content = forms.CharField(widget= forms.Textarea(attrs={'class':'form-control'}))
	img = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class':'form-control'}))
	time = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'class':'form-control'}))

	class Meta():
		model = Blog
		fields = '__all__'

    
            
        



class TeamForm(forms.ModelForm):
	team_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	profile = forms.ImageField(widget= forms.ClearableFileInput(attrs={'class':'form-control'}))
	title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))

	class Meta():
		model = Team
		exclude = ('created', 'modified')
    

    


class EngineForm(forms.ModelForm):
	engine_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

	class Meta():
		model = Car_Engine
		fields = ('engine_name',)

    


class ContactDealerForm(forms.ModelForm):
	name = forms.CharField(widget= forms.TextInput(attrs={'class':'form-control'}))
	phone = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control'}))
	email = forms.EmailField(widget= forms.EmailInput(attrs={'class':'form-control'}))
	location_id = forms.ModelChoiceField(queryset= Location.objects.all(), 
	widget= forms.Select(attrs={'class':'form-control'}), 
	empty_label= 'Select location'
	)
	dealer_id = forms.ModelChoiceField(queryset= User.objects.all(), 
	widget=forms.Select(attrs={'class':'form-control'}), 
	empty_label= 'Select a user'
	)

	class Meta():
		model = Contact_Dealer
		fields = ('__all__')
       







