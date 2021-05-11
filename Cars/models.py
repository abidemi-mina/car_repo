from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse

# Create your models here.

class DealerInfo(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Dealer')
    phone = models.CharField(max_length=17)
    website = models.URLField(blank=True, null=True)
    profile = models.ImageField(blank=True, null=True, upload_to='uploads/profile')
    biography = models.TextField()
    address = models.TextField()

    def __str__(self):
        return self.name
    
    class Meta():
        verbose_name_plural = 'DealerInfo'



class Brands(models.Model):
    name = models.CharField(max_length=30)
    image = models.FileField()
    
    def __str__(self):
        return self.name
    
    class Meta():
        verbose_name_plural = 'Brand'



class Location(models.Model):
    name =models.CharField(max_length=150, unique=True)

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



    car_name = models.OneToOneField(User,on_delete=models.CASCADE)
    location_id = models.ForeignKey(Location,related_name='car_location', on_delete=models.CASCADE)
    color = models.CharField(max_length=20)
    slug = models.SlugField(max_length=200)
    status = models.CharField(max_length= 10 ,choices=CONDITION, default=CHOOSE )
    prize = models. DecimalField(max_digits=9, decimal_places=2)
    make = models.ForeignKey(Brands,related_name='car_brand', on_delete=models.CASCADE)
    car_image1 = models.ImageField(blank=True, null=True, upload_to='uploads/profile')
    car_image2 = models.ImageField(blank=True, null=True, upload_to='uploads/profile')
    car_image3 = models.ImageField(blank=True, null=True, upload_to='uploads/profile')
    car_type = models.CharField(max_length=20)
    car_description = models.TextField(blank=True, null=True)
    manufacturing_date = models.DateField()
    offer_type = models.CharField(max_length=10, choices=OFFER_TYPE, default=CHOOSE)
    maintenance = models.TextField()
    transmission = models.CharField(max_length=20, choices=SELECT, default=CHOOSE)
    created= models.DateTimeField(auto_now_add=True)
    sponsored= models.DateTimeField(auto_now=True)
    featured= models.DateTimeField(auto_now=True)
    approve = models.BooleanField(default=False)

    def approve_car(self):
        self.approve = True
        self.save()
    
    def disapprove_car(self):
        self.approve = False
        self.save()


    
    class Meta():
        verbose_name_plural = 'Car'

    def __str__(self):
        return self.car_name

class Blog(models.Model):
    title = models.TextField()
    author = models.CharField(max_length=30)
    content = models.TextField()
    img = models.ImageField(blank=True, null=True)
    time = models.DateTimeField(auto_now_add=True)

    class Meta():
        verbose_name_plural = 'Blog'

    def __str__(self):
        return self.title



class Team(models.Model):
    team_name = models.CharField(max_length=120)
    profile = models.ImageField(blank=True, null=True, upload_to='uploads/profile')
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
    
    class Meta():
        verbose_name_plural = 'carType'


class CarEngine(models.Model):
    
    engine_name = models.CharField(max_length=30)

    def __str__(self):
        return self.engine_name
    
    class Meta():
        verbose_name_plural = 'carEngine'


class ContactDealer(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=17)
    location_id = models.ForeignKey(Location, on_delete=models.CASCADE)
    dealer_id = models.ForeignKey(User, on_delete=models.CASCADE)


    class Meta():
        verbose_name_plural = 'ContactDealer'


    def __str__(self):
        return self.name




