from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import logout
from django.contrib import messages
from backend.forms import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm 
from django.contrib.auth import update_session_auth_hash 
from Cars.models import Cars
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/pages/login-view/')
def index(request):
    return render(request, 'backend/index.html')

@login_required(login_url='/pages/login-view/')
def addlisting(request):
    return render(request, 'backend/add-listing.html')

@login_required(login_url='/pages/login-view/')
def changepas(request):
    if request == 'POST':
        changepas = ChangePas(data=request.POST, user=request.user) 
        if changepas.is_valid(): 
            changepas.save() 
            update_session_auth_hash(request, changepas.user) 
            messages.success(request, 'Password changed successfully.')
        else:
            messages.error('Correct the error below') 
    else: 
        changepas = ChangePas(user=request.user) 
    return render (request, 'backend/change-password.html', {'pas':changepas})

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
    return render(request, 'backend/add-listings.html')

def addlocation(request):
    return render(request, 'backend/add-location.html')


def createlist(request):
    return render(request, 'backend/create-listings.html')

def editlist(request):
    return render(request, 'backend/edit-listings.html')

def userprofile(request):
    return render(request, 'backend/user-profile.html')

def viewlist(request):
    return render(request, 'backend/view-listings.html')

def viewlocation(request):
    return render(request, 'backend/view-location.html')

def admin_logout(request):
    logout(request)
    return redirect('Cars:login_view')

@login_required(login_url='/pages/login-view/')
def confirm_logout(request):
    return render(request, 'backend/index.html')
