from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse 
from Cars.models import *
from Cars.forms import *
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from Cars.models import Blog
from .forms import CommentForm



from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from django.contrib import messages



# Create your views here.
def home(request):
    sale = Cars.objects.filter(offer_type='Sale')[:4]
    rent = Cars.objects.filter(offer_type='Rent')[:4]
    detail = Blog.objects.all()
    foreign = Cars.objects.filter(status='Foreign Used')[:4]
    New = Cars.objects.filter(status='New')[:4]
    location = Location.objects.all()
    milleage = Cars.objects.values_list('milleage')
    args = {'sale': sale, 'rent':rent, 'New':New, 'foreign':foreign,'location':location, 'milleage': milleage, 'det':detail}
    return render(request, 'htmls/index.html', args )

def about(request):
    return render(request, 'htmls/about.html')


def blog_detail(request,pk):
    blogdetail = Blog.objects.get(pk=pk)
    single_post = get_object_or_404(Blog, pk=pk)
    comments = Comment.objects.filter(post=pk).order_by('-time')
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = single_post
            comment.save()
            return redirect('Cars:blog_detail', pk=single_post.pk)
            # single_post = {'form': form}
    else:
        form = CommentForm()
    
    
    return render(request, 'htmls/blog-details.html', {'post':blogdetail, 'comm':comments, 'form':form, 'sipst':single_post}) 
                                                      

def contacts(request):
    if request.method =='POST':
        name = request.POST.get('name')
        lastname = request.POST.get('lastname')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')
        subject = 'Contact Us'
        context = {
            'name':name,
            'lastname':lastname,
            'phone' :phone,
            'email':email,
            'message':message,
            
        }
        
        html_message = render_to_string('htmls/mail.html', context)
        plain_message = strip_tags(html_message)
        from_email = 'Car Website <alayandesteven@gmail.com>'
        send = mail.send_mail(subject, plain_message,from_email[
                        'alayandesteven@gmail.com', 'aminatmide@gmail.com', email], html_message=html_message, fail_silently=True)
        if send:
            messages.success(request, 'Email sent, we will reply you shorty!')
        else:
            messages.error('Mail not sent')
    return render(request, 'htmls/contact.html')


   
 
    


def blog(request):
    blog_post = Blog.objects.order_by('-time')
    return render(request, 'htmls/blog.html', {'blog':blog_post})
    
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

def cars(request):
    car = Cars.objects.order_by('-created')
    return render(request, 'htmls/cars.html', {'coo':car})

def team(request):
    team = Team.objects.order_by('-created')
    return render(request, 'htmls/team.html', {'team_key':team})

def team_details(request, team_id):
    detail = Team.objects.get(id=team_id)
    return render(request, 'htmls/team-details.html', {'det':detail})
   

