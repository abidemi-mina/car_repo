from django import forms
from Cars.models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
	username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control'}))
	first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
	password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))

	class Meta():
		model = User
		fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

	def save(self, commit=True):
	    user = super().save(commit=False)
	    user.username = self.cleaned_data['username']
	    user.first_name = self.cleaned_data['first_name']
	    user.last_name = self.cleaned_data['last_name']
	    user.email = self.cleaned_data['email']

	    if commit:
	        user.save()
	        return user


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
	manufacturing_date = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control'}))

	class Meta():
		model = Cars
		exclude = ('created', 'slug', 'approve',)





	


class BrandForm(forms.ModelForm):
	name = forms.CharField(widget=forms.Select())

	class Meta():
		model = Brands
		fields = '__all__'


class CarTypeForm(forms.ModelForm):
	SEDAN = 'Sedan'
	COUPE = 'Coupe'
	SUV = 'SUV'
	TRUCK = 'Truck'
	HATCHBACK = 'Hatchback'
	WAGON = 'Wagon'
	CROSSOVER = 'Crossover'
	CONVERTIBLE = 'Convertible'
	SPORTCAR = 'Sport Car'
	MVP = 'MVP'
	SELECT = ''
	TYPES = [
		(SEDAN, 'Sedan(car)'),
		(COUPE,'Coupe'),
		(SUV,'SUV'),
		(TRUCK, 'Truck'),
		(HATCHBACK, 'Hatchback'),
		(CROSSOVER, 'Crossover'),
		(CONVERTIBLE, 'Convertible'),
		(SPORTCAR, 'Sport Car'),
		(MVP, 'MVP'),
		(SELECT, 'Select An Car Type'),
	]

	names = forms.CharField(widget=forms.Select(choices=TYPES),)
	class Meta():
		model = Car_Type
		fields =('names',)

class FilterForm(forms.ModelForm):
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
		widget=forms.Select(),
		empty_label= 'Select maker'
	)
	vehicle_type= forms.ModelChoiceField(
		queryset=Car_Type.objects.all(),
		widget=forms.Select(),
		empty_label='Select vehicle type '
	)
	offer_type = forms.CharField(widget=forms.Select(choices=OFFER_TYPE),) 
	transmission = forms.CharField(widget=forms.Select(choices=SELECT),)


	class Meta():
		model = Cars
		fields = ( 'make', 'offer_type','transmission','vehicle_type')

class CommentForm(forms.ModelForm):
	name = forms.CharField(widget=forms.TextInput())
	comment = forms.CharField(widget=forms.Textarea(attrs={
		'class': 'form-control',
		'placeholder': 'Type your comment',
		'rows' : '4',
	}))

	class Meta():
		model = Comment
		fields = ('name', 'comment' )



