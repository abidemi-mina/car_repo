from django.shortcuts import render,redirect
from django.http import HttpResponse 
from Cars.models import *


from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required



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


def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            if request.user.is_superuser:

                login(request,user)
                return redirect('backend:index')
            else:
                login(request,user)
                return redirect('Cars:dashboard')
        else:
            messages.error(request, 'Name and Password do not match')

    return render(request, 'htmls/login.html')

def logout(request):
    return render(request, 'htmls/logout.html')

@login_required(login_url='/pages/login-view/')
def dashboard(request):
    return render(request, 'htmls/dashboard.html')

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
   

