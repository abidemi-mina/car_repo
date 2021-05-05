from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse

# Create your models here.
class Brands(models.Model):
    name = models.CharField(max_length=30)
    image = models.FileField()
    
    def __str__(self):
        return self.name


 
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


    name = models.OneToOneField(User,on_delete=models.CASCADE)
    location = models.CharField(max_length=30)
    color = models.CharField(max_length=20)
    slug = models.SlugField(max_length=200)
    status = models.CharField(max_length= 10 ,choices=CONDITION, default=CHOOSE )
    prize = models. DecimalField(max_digits=9, decimal_places=2)
    make = models.ForeignKey(Brands,related_name='car_brand', on_delete=models.CASCADE)
    image = models.FileField()
    car_type = models.CharField(max_length=20)
    description = models.TextField()
    manufacturing_date = models.DateField()
    offer_type = models.CharField(max_length=10, choices=OFFER_TYPE, default=CHOOSE)
    maintenance = models.TextField()
    gearbox = models.CharField(max_length=20)
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




