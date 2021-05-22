from django.shortcuts import render
from django.http import HttpResponse 
from Cars.models import *


# Create your views here.
def home(request):
    sale = Cars.objects.filter(offer_type='Sale')[:4]
    rent = Cars.objects.filter(offer_type='Rent')[:4]
    new = Cars.objects.order_by('-created')[:4]
    foreign = Cars.objects.order_by('-created')[:4]
    search = Cars.objects.all

    return render(request, 'htmls/index.html', {'sale': sale, 'rent':rent, 'new':new, 'foreign':foreign, 'srh':search})

def about(request):
    
    return render(request, 'htmls/about.html')
def blog_detail(request):
    return render(request, 'htmls/blog-details.html')
def blog(request):
    return render(request, 'htmls/blog.html')
    
def car_detail(request, car_id):
    detail = Cars.objects.get(id=car_id)
    contact = Contact_Dealer.objects.all
    return render(request, 'htmls/car-details.html', {'det':detail, 'cont':contact})


def login(request):
    return render(request, 'htmls/login.html')

def logout(request):
    return render(request, 'htmls/logout.html')

def register(request):
    return render(request, 'htmls/register.html')

def cars(request):
    car = Cars.objects.order_by('-created')
    return render(request, 'htmls/cars.html', {'coo':car})

def contact(request):
    return render(request, 'htmls/contact.html')

def team(request):
    team = Team.objects.order_by('-created')
    return render(request, 'htmls/team.html', {'team_key':team})

def team_details(request, team_id):
    detail = Team.objects.get(id=team_id)
    return render(request, 'htmls/team-details.html', {'det':detail})
   

