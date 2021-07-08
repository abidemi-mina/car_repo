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
    coto = Car_Type.objects.all()
    cnt = Cars.objects.order_by('created').count()
    return render(request, 'backend/view-cars.html', { 'cot':coto, 'cnt':cnt})

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
    sal = Cars.objects.filter(offer_type='Sale').count()
    ren = Cars.objects.filter(offer_type='Rent').count()
    fore = Cars.objects.filter(status='Foreign Used').count()
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

def userprofile(request, prop_id):
    dealer = Dealer_Info.objects.get(id=prop_id)
    return render(request, 'backend/user-profile.html', {'dealer' : dealer})

def updateprofile(request, prop_id):
    dealer = get_object_or_404( id=prop_id)
    if request.method == 'POST':
        edit_property = DealerForm(request.POST, request.FILES, instance=dealer)
        if edit_property.is_valid():
            user = edit_property.save(commit=False)
            # user.agent_id = request.user
            user.save()
            messages.success(request, 'Property edited')
    else:
        edit_property = DealerForm(instance=dealer)
    return render(request, 'backend/update-profile.html', {'dealer' : edit_property})

def createprofile(request , prop_id):
    user = DealerForm()
    if request.method == 'POST':
        user = DealerForm(request.POST, request.FILES )
        if user.is_valid():
            vp = user.save(commit=False)
            vp.save()
            messages.success(request, 'profile created')
    else:
        user = DealerForm()
    return render(request, 'backend/create-profile.html', {'dealer' : user})

def viewlist(request):
    newlist = Cars.objects.order_by('created')
    countlist = Cars.objects.order_by('created').count()
    return render(request, 'backend/view-listings.html' , {'new': newlist, 'cnt': countlist})

def viewlocation(request):
    viewlocations = Cars.objects.all()
    viewcount = Cars.objects.all().count()
    return render(request, 'backend/view-location.html', {'view' : viewlocations, 'count':viewcount})

def admin_logout(request):
    logout(request)
    return redirect('Cars:login_view')

@login_required(login_url='/pages/login-view/')
def confirm_logout(request):
    return render(request, 'backend/index.html')



@login_required(login_url='/pages/login-view/')
def delete(request, prop_id):
    single = get_object_or_404(Cars, pk=prop_id)
    single.delete()
    messages.success(request, 'Car Deleted successfully')
    return redirect('backend:viewlist')

@login_required(login_url='/pages/login-view/')
def approve_car(request, approve):
    post = get_object_or_404(Cars, pk=approve)
    post.approve_car()
    messages.success(request, 'Car approved successfully')
    return redirect('backend:viewlist')

@login_required(login_url='/pages/login-view/')
def disapprove_car(request, disapprove):
    post = get_object_or_404(Cars, pk=disapprove)
    post.disapprove_car()
    messages.error(request, 'Car disapproved successfully')
    return redirect('backend:viewlist')



@login_required(login_url='/pages/login-view/')
def delete_cartype(request, car):
    single = get_object_or_404(Car_Type, pk=car)
    single.delete()
    messages.success(request, 'Car type Deleted successfully')
    return redirect('backend:view-cars')

@login_required(login_url='/pages/login-page/')
def edit_list(request, prop_id):
    get_prop_record = get_object_or_404(Cars, id=prop_id)
    if request.method == 'POST':
        edit_property = CarForm(request.POST, request.FILES, instance=get_prop_record)
        if edit_property.is_valid():
            user = edit_property.save(commit=False)
            user.agent_id = request.user
            user.save()
            messages.success(request, 'Property edited')
    else:
        edit_property = CarForm(instance=get_prop_record)
    return render(request, 'backend/edit-listings.html', {'edit':edit_property})


