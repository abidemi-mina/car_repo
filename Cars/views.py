from django.shortcuts import render,redirect
from django.http import HttpResponse 
from Cars.models import *
from Cars.forms import *
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from Cars.models import Blog
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes




# Create your views here.
def home(request):
    sale = Cars.objects.filter(offer_type='Sale')[:4]
    rent = Cars.objects.filter(offer_type='Rent')[:4]
    detail = Blog.objects.all()
    foreign = Cars.objects.filter(status='Foreign Used')[:4]
    New = Cars.objects.filter(status='New')[:4]
    location = Location.objects.all()
    milleage = Cars.objects.values_list('milleage')
    filter_obj = FilterForm()
    args = {'sale': sale, 'rent':rent, 'New':New, 'foreign':foreign,'location':location, 'milleage': milleage, 'det':detail, 'fil':filter_obj}
    return render(request, 'htmls/index.html', args)

def about(request):
    
    return render(request, 'htmls/about.html')
def blog_detail(request, blog_id):
    blogdetail = Blog.objects.get(id=blog_id)
    return render(request, 'htmls/blog-details.html', {'post':blogdetail})

def blog(request):
    blog_post = Blog.objects.order_by('-time')
    return render(request, 'htmls/blog.html', {'blog':blog_post})
    
def car_detail(request, car_id):
    detail = Cars.objects.get(id=car_id)
    # contact = Contact_Dealer.objects.all
    return render(request, 'htmls/car-details.html', {'det':detail})


def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.is_superuser == True :  
                login(request,user)
                return redirect('backend:index')
            elif not(user.is_superuser):
                login(request,user)
                return redirect('Cars:dashboard')
        else:
            messages.error(request, 'Name and Password do not match')

    return render(request, 'htmls/login.html')


    

def logout(request):
    return render(request, 'htmls/logout.html')

@login_required(login_url='/pages/login-view/')
def dashboard(request):
    sale = Cars.objects.filter(offer_type='Sale').count()
    rent = Cars.objects.filter(offer_type='Rent').count()
    foreign = Cars.objects.filter(status='Foreign Used').count()
    New = Cars.objects.filter(status='New').count()
    All = Cars.objects.all().count()
    return render(request, 'htmls/dashboard.html',{'salec': sale, 'rentc':rent, 'Newc':New, 'foreignc':foreign , 'Allc':All})


def register(request):
    register = RegisterForm()
    if request.method == 'POST':
        register = RegisterForm(request.POST)
        if register.is_valid():
            register.save()
            messages.success(request, 'User Registered ')
    else:
        register = RegisterForm()
    return render(request, 'htmls/register.html', {'reg':register})
    
# def resetpass(request):
#     reset = RegisterForm()
#     if request.method == 'POST':
#         reset = RegisterForm(request.POST)
#         if reset.is_valid():
#             reset.save()
#             messages.success(request, 'User Registered ')
#     else:
#         reset = RegisterForm()
#     return render(request, 'htmls/register.html', {'res':reset})

def cars(request):
    moto = Cars.objects.order_by('-created')[:4]
    coto = Cars.objects.order_by('created')[:4]
    return render(request, 'htmls/cars.html', {'coo':moto, 'cot':coto})

def contact(request):
    return render(request, 'htmls/contact.html')

def team(request):
    team = Team.objects.order_by('-created')
    return render(request, 'htmls/team.html', {'team_key':team})

def team_details(request, team_id):
    detail = Team.objects.get(id=team_id)
    return render(request, 'htmls/team-details.html', {'det':detail})
def commentsec (request):
    return render(request)
   

def filter_form(request):
    if request.method == 'GET':
        filter_form = FilterForm(request.GET)
        if filter_form.is_valid():
            print('correct')
            make = filter_form.cleaned_data.get('make')
            offer_type = filter_form.cleaned_data.get('offer_type')
            vehicle_type = filter_form.cleaned_data.get('vehicle_type')
            transmission = filter_form.cleaned_data.get('transmission')
            filter_query = Cars.objects.filter(make=make)
            return render(request, 'htmls/outcome.html', {'filter':filter_query})
        else :
            print('No data')
    return render(request, 'htmls/outcome.html')

def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "htmls/password-reset-email.txt"
					c = {
					"email":user.email,
					'domain':'127.0.0.1:8000',
					'site_name': 'Website',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, 'admin@example.com' , [user.email], fail_silently=False)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					return redirect ("/password_reset/done/")
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="htmls/password-reset.html", context={"password_reset_form":password_reset_form})