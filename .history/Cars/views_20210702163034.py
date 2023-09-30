from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse 
from Cars.models import *
from Cars.forms import *
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from Cars.models import Blog
from .forms import CommentForm
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.conf import settings




# EMAIL START HERE
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings

# EMAIL ENDS HERE




# from django.core import mail
# from .forms import ContactForm
# from django.core.mail import send_mail, BadHeaderError


from django.contrib import messages



# Create your views here.
def home(request):
    sale = Cars.objects.filter(offer_type='Sale')[:4]
    rent = Cars.objects.filter(offer_type='Rent')[:4]
    detail = Blog.objects.all()
    foreign = Cars.objects.filter(status='Foreign Used')[:4]
    New = Cars.objects.filter(status='New')[:4]
    location = Location.objects.all()
    filter_obj = FilterForm()
    args = {'sale': sale, 'rent':rent, 'New':New, 'foreign':foreign,'location':location, 'det':detail, 'fil':filter_obj}
    return render(request, 'htmls/index.html', args)

def home2(request):
    sale = Cars.objects.filter(offer_type='Sale')[:4]
    rent = Cars.objects.filter(offer_type='Rent')[:4]
    detail = Blog.objects.all()
    foreign = Cars.objects.filter(status='Foreign Used')[:4]
    New = Cars.objects.filter(status='New')[:4]
    location = Location.objects.all()
    filter_obj = FilterForm()
    args = {'sale': sale, 'rent':rent, 'New':New, 'foreign':foreign,'location':location, 'det':detail, 'fil':filter_obj}
    return render(request, 'backend/home-page.html', args)

def home3(request):
    sale = Cars.objects.filter(offer_type='Sale')[:4]
    rent = Cars.objects.filter(offer_type='Rent')[:4]
    detail = Blog.objects.all()
    foreign = Cars.objects.filter(status='Foreign Used')[:4]
    New = Cars.objects.filter(status='New')[:4]
    location = Location.objects.all()
    filter_obj = FilterForm()
    args = {'sale': sale, 'rent':rent, 'New':New, 'foreign':foreign,'location':location, 'det':detail, 'fil':filter_obj}
    return render(request, 'backend/home-page2.html', args)

def about(request):
    return render(request, 'htmls/about.html')


def blog_detail(request,pk):
    blogdetail = Blog.objects.get(pk=pk)
    single_post = get_object_or_404(Blog, pk=pk)
     comments = Comment.objects.filter(post=pk).order_by('-timestamp')
    comments = Comment.objects.filter(post=pk).order_by('-time',)[:6]
    if request.method == "POST":
        form = CommentForm(request.POST or None)
        if form.is_valid():
            # form.instance.Blog = request.Blog
            comment = form.save(commit=False) 
            comment.post = single_post
            
           
            form.save()
            return redirect('Cars:blog_detail', pk=single_post.pk)
        
            # single_post = {'form': form}
    else:
        form = CommentForm()
    return render(request, 'htmls/blog-details.html', {'post':blogdetail, 'comm':comments, 'form':form, 'sipst':single_post}) 
                                                      

def contact(request):
    if request.method =="POST":
        full_name = request.POST.get('full_name')
        email_address = request.POST.get('email_address')
        message = request.POST.get('message')

        
        subject = 'Contact Form'

        args ={
            'full_name':full_name,
            'email_address':email_address,
            'message':message
            
        }
        
        html_message = render_to_string('htmls/mail-template.html', args)
        plain_message = strip_tags(html_message)
        from_email = settings.EMAIL_FROM
        send = mail.send_mail(subject, plain_message, from_email,
                        ['jigih77129@seek4wap.com', 'jigih77129@seek4wap.com'], html_message=html_message)
        if send:
            print(send)
            messages.success(request, 'Email sent')
        else:
            messages.error(request, 'Email not sent')

    return render(request, 'htmls/contact.html')

        
  
   
            
       


   
 
    


def blog_detail2(request, blog_id):
    print(blog_id)
    blogdetail = Blog.objects.get(id=blog_id)
    return render(request, 'backend/blog-details2.html', {'post':blogdetail})

def blog_detail3(request, blog_id):
    
    blogdetail = Blog.objects.get(id=blog_id)
    return render(request, 'backend/blog-details3.html', {'post':blogdetail})

def blog(request):
    blog_post = Blog.objects.order_by('-time')
    return render(request, 'htmls/blog.html', {'blog':blog_post})

def blog2(request):
    blog_post = Blog.objects.order_by('-time')
    return render(request, 'backend/blog2.html', {'blog':blog_post})
    
def blog3(request):
    blog_post = Blog.objects.order_by('-time')
    return render(request, 'backend/blog3.html', {'blog':blog_post})
    
def car_detail(request, car_id):
    detail = Cars.objects.get(id=car_id)
    # contact = Contact_Dealer.objects.all
    return render(request, 'htmls/car-details.html', {'det':detail})

def car_detail2(request, car_id):
    detail = Cars.objects.get(id=car_id)
    # contact = Contact_Dealer.objects.all
    return render(request, 'backend/car-details2.html', {'det':detail})

def car_detail3(request, car_id):
    detail = Cars.objects.get(id=car_id)
    # contact = Contact_Dealer.objects.all
    return render(request, 'backend/car-details3.html', {'det':detail})


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
    return render(request, 'htmls/add-property.html' , {'add': add_car})

@login_required(login_url='/pages/login-view/')
def addlistings2(request):
    if request.method == 'POST':
        add_car = CarForm(request.POST, request.FILES)
        if add_car.is_valid():
            user = add_car.save(commit=False)
            user.save()
            messages.success(request, 'Car added')
    else:
        add_car =  CarForm()
    return render(request, 'htmls/add-property.html' , {'add': add_car})

    
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
    filterb = FilterForm()
    return render(request, 'htmls/cars.html', {'coo':moto, 'cot':coto,'filt': filterb} )

def cars2(request):
    moto = Cars.objects.order_by('-created')[:4]
    coto = Cars.objects.order_by('created')[:4]
    filterb = FilterForm()
    return render(request, 'backend/cars2.html', {'coo':moto, 'cot':coto,'filt': filterb} )

def cars3(request):
    moto = Cars.objects.order_by('-created')[:4]
    coto = Cars.objects.order_by('created')[:4]
    filterb = FilterForm()
    return render(request, 'backend/cars3.html', {'coo':moto, 'cot':coto,'filt': filterb} )

# def contact(request):
#     return render(request, 'htmls/contact.html')

def team(request):
    team = Team.objects.order_by('-created')
    return render(request, 'htmls/team.html', {'team_key':team})

def team2(request):
    team = Team.objects.order_by('-created')
    return render(request, 'backend/team2.html', {'team_key':team})

def team3(request):
    team = Team.objects.order_by('-created')
    return render(request, 'backend/team3.html', {'team_key':team})

def team_details(request, team_id):
    detail = Team.objects.get(id=team_id)
    return render(request, 'htmls/team-details.html', {'det':detail})

def team_details2(request, team_id):
    detail = Team.objects.get(id=team_id)
    return render(request, 'backend/team-details2.html', {'det':detail})

def team_details3(request, team_id):
    detail = Team.objects.get(id=team_id)
    return render(request, 'backend/team-details3.html', {'det':detail})


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
						send_mail(subject, email, 'aminatabidemi212@gmail.com' , [user.email], fail_silently=True)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					return redirect ("/password_reset/done/")
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="htmls/password-reset.html", context={"password_reset_form":password_reset_form})