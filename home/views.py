from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib  import auth,messages
from django.http import JsonResponse
# Create your views here.


def index(request):
    if request.user.is_authenticated:
        return render(request,'home.html')
    else:
        return render(request,'index.html')

@login_required(login_url="login")
def home(request):
        return render(request,'auth.html')


def log_in(request):
    if request.method == "POST" :
        username = request.POST['user_name']
        userpass = request.POST['user_pass']
        
        try:
            user = auth.authenticate(username=username, password=userpass)
            auth.login(request,user)
            json = {'status' : 'success'}
            return JsonResponse(json)
        except:
            json = {
                'status' : 'error',
                'message' : 'Invalid username or passwod'
            }
            return JsonResponse(json)

    else:
        json = {
            'status' : 'error',
            'message' : 'No data provided'
        }
        return JsonResponse(json)


def signup(request):
    if request.method == "POST" :
        useremail = request.POST['user_email']
        username = request.POST['user_name']
        userpass = request.POST['user_pass']
         # check if user does not exist
        if User.objects.filter(username=username).exists():
            json = {
                'status' : 'error',
                'message' : 'Username already exist'
            }
            return JsonResponse(json)

        elif User.objects.filter(email=useremail).exists():
            json = {
                'status' : 'error',
                'message' : 'Email already exist'
            }
            return JsonResponse(json)

        else :
            create_new_user = User.objects.create_user(username, useremail, userpass)
            create_new_user.save()
            user = auth.authenticate(username=username, password=userpass)
            auth.login(request, user)

            if create_new_user is not None:
                if create_new_user.is_active:
                    json = { 'status' : 'success'}
                    return JsonResponse(json)
                else:
                    json = {'status' : 'error',
                    'message' : 'The password is valid, but the account has been disabled!'
                    }
                    return JsonResponse(json)

    else:
        json = {
            'status' : 'error',
            'message' : 'No data provided'
        }
        return JsonResponse(json)


def signout(request):
    auth.logout(request)
    return redirect('index')
