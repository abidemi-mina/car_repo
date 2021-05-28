from django.shortcuts import render,redirect


from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'backend/index.html')

def addlisting(request):
    return render(request, 'backend/add-listing.html')

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
