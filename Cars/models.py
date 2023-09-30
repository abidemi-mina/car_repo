from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.exceptions import ObjectDoesNotExist

# Create your models here.

class Dealer_Info(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Dealer')
    phone = models.CharField(max_length=17)
    website = models.URLField(blank=True, null=True)
    profile = models.ImageField(blank=True, null=True, upload_to='uploads/profile')
    biography = models.TextField()
    address = models.TextField()


    def img_url(self):
        if self.profile:
            return self.profile.url
        else:
            return '/static/public/images/img_1.jpg'



    def __str__(self):
        return str(self.user_id)

    class Meta():
        verbose_name_plural = 'Dealer Info'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=150)
    signup_confirmation = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    try:
        instance.profile.save()
    except ObjectDoesNotExist:
        Profile.objects.create(user=instance)



class Brands(models.Model):
    name = models.CharField(max_length=30)


    def __str__(self):
        return self.name

    class Meta():
        verbose_name_plural = 'Brands'



class Location(models.Model):
    name =models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.name

    class Meta():
        verbose_name_plural = 'Location'


class Car_Type(models.Model):
    names = models.CharField(max_length=30)

    def __str__(self):
        return self.names

    class Meta():
        verbose_name_plural = 'Car Type'




class Cars(models.Model):
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


    car_model = models.CharField(max_length=200)
    location_id = models.ForeignKey(Location,related_name='car_location', on_delete=models.CASCADE)
    color = models.CharField(max_length=20)
    slug = models.SlugField(max_length=200)
    status = models.CharField(max_length=15 ,choices=CONDITION, default=CHOOSE )
    prize = models.DecimalField(max_digits=9, decimal_places=2)
    old_prize = models.DecimalField(max_digits=9, decimal_places=2 ,null=True)
    make = models.ForeignKey(Brands,related_name='car_brand', on_delete=models.CASCADE)
    car_image = models.ImageField(blank=True, null=True, upload_to='uploads/profile')
    car_image1 = models.ImageField(blank=True, null=True, upload_to='uploads/profile')
    car_image2 = models.ImageField(blank=True, null=True, upload_to='uploads/profile')
    car_image3 = models.ImageField(blank=True, null=True, upload_to='uploads/profile')
    vehicle_type = models.ForeignKey(Car_Type,related_name='vehicle_type', on_delete=models.CASCADE)
    car_description = models.TextField(blank=True, null=True)
    manufacturing_date = models.DateField(null=True, blank=True)
    offer_type = models.CharField(max_length=10, choices=OFFER_TYPE, default=CHOOSE)
    maintenance = models.TextField()
    transmission = models.CharField(max_length=20, choices=SELECT, default=CHOOSE)
    milleage = models.CharField(max_length=20)
    first_registration = models.CharField(max_length=50)
    fuel = models.CharField(max_length=50)
    created= models.DateTimeField(auto_now_add=True)
    approve = models.BooleanField(default=False)



    def img_url(self):
        if self.car_image:
            return self.car_image.url
        else:
            return '/static/public/images/img_1.jpg'


    def img_url1(self):
        if self.car_image1:
            return self.car_image1.url
        else:
            return '/static/public/images/img_1.jpg'

    def img_url2(self):
        if self.car_image2.url:
            return self.car_image2.url
        else:
            return '/static/public/images/img_1.jpg'

    def img_url3(self):
        if self.car_image3.url:
            return self.car_image3.url
        else:
            return '/static/public/images/img_1.jpg'

    def approve_car(self):
        self.approve = True
        self.save()

    def disapprove_car(self):
        self.approve = False
        self.save()



    class Meta():
        verbose_name_plural = 'Car'

    def __str__(self):
        return self.car_model




class Blog(models.Model):

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




    title = models.TextField()
    author = models.ForeignKey(User, related_name="author", on_delete=models.CASCADE)
    category = models.CharField(max_length=100, choices=SELECT, default=CHOOSE)
    content = models.TextField(verbose_name= 'Content')
    img = models.ImageField(blank=True, null=True)
    time = models.DateTimeField(auto_now_add=True)

    class Meta():
        verbose_name_plural = 'Blog'

    def __str__(self):
        return self.title

    @property
    def img_url(self):
        if self.img.url:
            return self.img.url
        else:
              return '/static/public/images/img_1.jpg'



class Comment(models.Model):
    post = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comment')
    name = models.CharField(max_length=50)
    email = models.EmailField()
    content = models.TextField(verbose_name= 'Content')
    time = models.DateField(auto_now_add=True)
    active = models.BooleanField(default=False)



    def __str__(self):
        return self.name

    class Meta():
        verbose_name_plural = 'Comment'











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




class Car_Engine(models.Model):

    engine_name = models.CharField(max_length=30)

    def __str__(self):
        return self.engine_name

    class Meta():
        verbose_name_plural = 'Car Engine'


class Contact_Dealer(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=17)
    email = models.EmailField(max_length=200)
    location_id = models.ForeignKey(Location, on_delete=models.CASCADE)
    dealer_id = models.ForeignKey(User, on_delete=models.CASCADE)


    class Meta():
        verbose_name_plural = 'Contact Dealer'


    def __str__(self):
        return self.name




