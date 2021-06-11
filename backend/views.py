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
    return render(request, 'backend/add-listings.html')
@login_required(login_url='/pages/login-view/')
def viewcars(request):
    return render(request, 'backend/view-cars.html')

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
