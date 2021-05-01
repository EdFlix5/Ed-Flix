from home.models import FileUpload
from django.contrib  import auth
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.shortcuts import redirect
from django.http import JsonResponse
from django.contrib.auth import get_user_model
import re

User = get_user_model()

def login(request):
    if request.method == "POST" :
        username = request.POST['user_name']
        userpass = request.POST['user_pass']
        
        try:
            # regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
            # if(re.search(regex,usernameOrEmail)):
            #     username = User.objects.get(email = usernameOrEmail)
            #     user = auth.authenticate(username=username, password=userpass)
            # else:
            user = auth.authenticate(username=username, password=userpass)
            auth.login(request,user)
            json = {'status' : 'success'}
            return JsonResponse(json)
        except:
            json = {
                'status' : 'error',
                'message' : 'Invalid Credentials'
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



@login_required(login_url="login")
def upload_file(request):
    if request.method == "POST" and request.FILES['file']:
        file = request.FILES['file']
        fs = FileSystemStorage("Uploads")
        filename = fs.save(file.name, file)
        uploaded_file_url = fs.url(filename)
        title = request.POST.get('title')
        author = request.POST.get('author')
        subject = request.POST.get('subject')

        fileUpload = FileUpload(title = title, author = author, subject=subject)
        fileUpload.save()
        
        reply = {"success" : "file uploaded successfully","file-url": uploaded_file_url}
        return JsonResponse(reply)

    reply = {"error" : "No File Provided"}
    return JsonResponse(reply)
