from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import logout
from django.contrib import messages
from backend.forms import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm 
from django.contrib.auth import update_session_auth_hash 
from Cars.models import *
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/pages/login-view/')
def index(request):
    return render(request, 'backend/index.html')

def viewcars(request):
    moto = Cars.objects.order_by('-created')[:4]
    coto = Cars.objects.order_by('created')[:4]
    return render(request, 'backend/view-cars.html', {'coo':moto, 'cot':coto})

@login_required(login_url='/pages/login-view/')

@login_required(login_url='/pages/login-view/')
def change_password(request):
    if request.method == 'POST':
        form = ChangeWord(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            # return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = ChangeWord(request.user)
    return render(request, 'backend/change-password.html', {'form': form})

# def change_password(request):
    # if request.method == 'POST':
    #     form = PasswordChangeForm(request.user, request.POST)
    #     if form.is_valid():
    #         user = form.save()
    #         update_session_auth_hash(request, user)  # Important!
    #         messages.success(request, 'Your password was successfully updated!')
    #         return redirect('change_password')
    #     else:
    #         messages.error(request, 'Please correct the error below.')
    # else:
    #     form = PasswordChangeForm(request.user)
    # return render(request, 'accounts/change_password.html', {'form': form})
    

@login_required(login_url='/pages/login-view/')
def admin(request):
    sale = Cars.objects.filter(offer_type='Sale').count()
    rent = Cars.objects.filter(offer_type='Rent').count()
    foreign = Cars.objects.filter(status='Foreign Used').count()
    New = Cars.objects.filter(status='New').count()
    All = Cars.objects.all().count()
    return render(request, 'backend/admin_base.html', {'sal': sale, 'ren':rent, 'New':New, 'foreign':foreign , 'All':All})


    
@login_required(login_url='/pages/login-view/')
def addlistings(request):
    if request.method == 'POST':
        add_car = CarForm(request.POST, request.FILES)
        if add_car.is_valid():
            user = add_car.save(commit=False)
            user.save()
            messages.success(request, 'Car added')
    else:
        add_car =  CarForm()
    return render(request, 'backend/add-listings.html' , {'add': add_car})
@login_required(login_url='/pages/login-view/')


def addlocation(request):
    location_form = LocationForm()
    if request.method == 'POST':
        location_form = LocationForm(request.POST)
        if location_form.is_valid():
            location_form.save()
            messages.success(request, 'Location Added')
    else:
        location_form = LocationForm()
    return render(request, 'backend/add-location.html', {'location' : location_form})


def addcar(request):
    car_type = CarTypeForm()
    if request.method == 'POST':
        car_type = CarTypeForm(request.POST)
        if car_type.is_valid():
            car_type.save()
            messages.success(request, 'Car Type  Added')
    else:
        car_type = CarTypeForm()
    return render(request, 'backend/add-cars.html', {'car' : car_type})


def createlist(request):
    return render(request, 'backend/create-listings.html')

def editlist(request):
    return render(request, 'backend/edit-listings.html')

def userprofile(request):
    dealer = Dealer_Info.objects.all()
    return render(request, 'backend/user-profile.html', {'dealer' : dealer})

def viewlist(request):
    newlist = Cars.objects.order_by('created')

    return render(request, 'backend/view-listings.html' , {'new': newlist})

def viewlocation(request):
    viewlocations = Cars.objects.all()
    return render(request, 'backend/view-location.html', {'view' : viewlocations})

def admin_logout(request):
    logout(request)
    return redirect('Cars:login_view')

@login_required(login_url='/pages/login-view/')
def confirm_logout(request):
    return render(request, 'backend/index.html')
