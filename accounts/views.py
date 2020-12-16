from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django import forms
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import EdFlixUserAuthenticationForm,EdFlixUserCreationForm


def signup(request):
    if request.method == 'POST':
        form = EdFlixUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'registration/signup.html', {'form': form})
    else:
        form = EdFlixUserCreationForm()
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return render(request, 'registration/signup.html', {'form': form})



def user_login(request):
    if request.method == "POST":
        form = EdFlixUserAuthenticationForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                login(request, user)
                # messages.info(request, f"You are now logged in as {username}") 
                return redirect(request.POST['next'])
            else:
                error = "Invalid username or password."
                return render(request,'registration/login.html',{'form':form,'error':error})
        else:
            error = "Invalid Credentials."
            return render(request,'registration/login.html',{'form':form,'error':error})
    else:
        if request.user.is_authenticated:
            return redirect('/')
        else:
            next = request.GET.get('next')
            if not next:
                next = "/"
            form = EdFlixUserAuthenticationForm()
            return render(request,'registration/login.html',{'form':form,'next':next})

def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("/")



