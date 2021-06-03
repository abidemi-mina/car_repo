from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.contrib import messages
from Cars.models import Cars
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/pages/login-view/')
def index(request):
    return render(request, 'backend/index.html')

def addlisting(request):
    return render(request, 'backend/add-listing.html')

def admin(request):
    sale = Cars.objects.filter(offer_type='Sale').count()
    rent = Cars.objects.filter(offer_type='Rent').count()
    foreign = Cars.objects.filter(status='Foreign Used').count()
    New = Cars.objects.filter(status='New').count()
    All = Cars.objects.all().count()
    return render(request, 'backend/admin_base.html', {'sal': sale, 'ren':rent, 'New':New, 'foreign':foreign , 'All':All})


    

def addlistings(request):
    return render(request, 'backend/add-listings.html')

def addlocation(request):
    return render(request, 'backend/add-location.html')

def changepas(request):
    return render(request, 'backend/change-password.html')

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
