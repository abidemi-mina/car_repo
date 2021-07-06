from django import forms
from Cars.models import *
from django.db.models import fields
from .models import Blog, Comment
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
     


class CommentForm(forms.ModelForm):
    name = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}))
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Type your comment',
        'id': 'usercomment',
        'rows': '4'
    }))
    class Meta:
        model = Comment
        fields = ('name', 'content' )
	
     
     
    
    
class BrandForm(forms.ModelForm):
	name = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))

	class Meta():
		model = Brands
		fields = '__all__'

 
class CarTypeForm(forms.ModelForm):
	names = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),)

	def clean_name(self):
		form_name = self.cleaned_data['names'].capitalize()
		value_name = Car_Type.objects.filter(name=form_name).exists()
		if value_name == True:
			raise forms.ValidationError('Car type already exist')
		return form_name

	class Meta():
		model = Car_Type
		fields =('names',)

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
		widget=forms.Select(attrs={'class':'form-control col-md-9'}),
		empty_label= 'Select maker'
	)
	vehicle_type= forms.ModelChoiceField(
		queryset=Car_Type.objects.all(),
		widget=forms.Select(attrs={'class':' form-control btn-outline-primary  col-md-7 rounded-0',}),
		empty_label='Select vehicle type '
	) 
	car_model = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control col-md-9'} ))
	location_id = forms.ModelChoiceField(
		queryset=Location.objects.all(),
		widget= forms.Select(attrs={'class':'form-control col-md-9'}),
		empty_label= 'Select your location'
	)
	milleage = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control font-weight-bold '}))
	status = forms.CharField(widget=forms.Select(choices=CONDITION, attrs={'class':'form-control col-md-9'}))
	color = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control col-md-7'}))
	car_description =forms.CharField(widget= forms.Textarea(attrs={'class':'form-control col-md-12'}))
	fuel = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control col-md-7'}))
	offer_type = forms.CharField(widget=forms.Select(choices=OFFER_TYPE, attrs={'class':'form-control col-md-7'}))
	transmission = forms.CharField(widget=forms.Select(choices=SELECT,attrs={'class':'form-control col-md-7'}))
	car_image = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class':'form-control col-md-9'}))
	car_image1 = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class':'form-control col-md-9'}))
	car_image2 = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class':'form-control col-md-9'}))
	car_image3 = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class':'form-control col-md-9'}))
	maintenance = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control col-md-12'}))
	prize = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'form-control col-md-7'}))
	old_prize = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'form-control col-md-7'}))
	first_registration = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control col-md-7'}))
	manufacturing_date = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control col-md-7'}))

	class Meta():
		model = Cars
		exclude = ('created', 'slug', 'approve',)





	






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
	content = forms.CharField(widget=forms.Textarea(attrs={
		'class': 'form-control',
		'placeholder': 'Type your comment',
		'rows' : '4',
	}))

	class Meta():
		model = Comment
		fields = ('name','content',)
		


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
       











