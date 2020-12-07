from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    if request.user.is_authenticated:
        return render(request,'home.html')
    else:
        return render(request,'index.html')


def explore(request):
    return render(request,'index_backup.html')

@login_required(login_url="login")
def home(request):
        return render(request,'auth.html')

