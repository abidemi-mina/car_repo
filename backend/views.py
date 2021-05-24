from django.shortcuts import render,redirect


from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'backend/index.html')


def admin_logout(request):
    logout(request)
    return redirect('Cars:login_view')
