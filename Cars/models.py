from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse

# Create your models here.
class Brands(models.Model):
    name = models.CharField(max_length=30)
    image = models.FileField()
    
    def __str__(self):
        return self.name



class Location(models.Model):
    name =models.CharField(max_length=150)

    def __str__(self):
        return self.name
    
    class Meta():
        verbose_name_plural = 'Location'



 
class Cars(models.Model):
    RENT = 'Rent'
    SALE = 'Sale'
    CHOOSE = ''
    OFFER_TYPE = [
        (RENT, 'Rent'),
        (SALE, 'Sale'),
        (CHOOSE, 'Choose An Offer Type'),
    ]

    USED = 'Used'
    NEW = 'New '
    CHOOSE = ''
    CONDITION = [
        (USED , 'Used'),
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



    name = models.OneToOneField(User,on_delete=models.CASCADE)
    location_id = models.ForeignKey(Location,related_name='Location', on_delete=models.CASCADE)
    color = models.CharField(max_length=20)
    slug = models.SlugField(max_length=200)
    status = models.CharField(max_length= 10 ,choices=CONDITION, default=CHOOSE )
    prize = models. DecimalField(max_digits=9, decimal_places=2)
    make = models.ForeignKey(Brands,related_name='car_brand', on_delete=models.CASCADE)
    car_image1 = models.ImageField(blank=True, null=True, upload_to='uploads/')
    car_image2 = models.ImageField(blank=True, null=True, upload_to='uploads/')
    car_image3 = models.ImageField(blank=True, null=True, upload_to='uploads/')
    car_type = models.CharField(max_length=20)
    description = models.TextField()
    manufacturing_date = models.DateField()
    offer_type = models.CharField(max_length=10, choices=OFFER_TYPE, default=CHOOSE)
    maintenance = models.TextField()
    transmission = models.CharField(max_length=20, choices=SELECT, default=CHOOSE)
    created= models.DateTimeField(auto_now_add=True)
    sponsored= models.DateTimeField(auto_now=True)
    featured= models.DateTimeField(auto_now=True)
    
    class Meta():
        verbose_name_plural = 'Cars'

    def __str__(self):
        return self.name


class Seller(models.Model):
    name = models.CharField(max_length=30)
    image = models.FileField()
    contact = models.CharField(max_length=11)
    description = models.TextField()

    def __str__(self):
        return self.name


class Team(models.Model):
    team_name = models.CharField(max_length=120)
    profile = models.ImageField(blank=True, null=True, upload_to='uploads/')
    title = models.CharField(max_length=100,blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.team_name
    
    class Meta():
        verbose_name_plural = 'Team'


    




class CarType(models.Model):
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
    CAR_TYPE = [
        (SEDAN, 'Sedan'),
        (COUPE,'Coupe'),
        (SUV,'SUV'),
        (TRUCK, 'Truck'),
        (HATCHBACK, 'Hatchback'),
        (CROSSOVER, 'Crossover'),
        (CONVERTIBLE, 'Convertible'),
        (SPORTCAR, 'Sport Car'),
        (MVP, 'MVP'),
        (SELECT, 'Select An Engine Type'),
    ]

    Type = models.OneToOneField(Cars,on_delete=models.CASCADE)
    def __str__(self):
        return self.Type


class CarEngine(models.Model):
    
    engine_name = models.CharField(max_length=30)

    def __str__(self):
        return self.engine_name




