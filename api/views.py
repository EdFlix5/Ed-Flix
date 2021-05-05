from accounts.models import DocViews
from django.http.response import HttpResponse
from .models import FileUpload
from django.contrib  import auth
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.shortcuts import redirect
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from .converter import longToSizeString
import pytesseract
import pdf2image
import re,json

 

def processPdf(pdf_path, lang_code):
    print(pdf_path)
    # pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    pages = pdf2image.convert_from_path(pdf_path=pdf_path, dpi=200, size=(1654,2340))
    text = ""
    for page in pages:
        text += pytesseract.image_to_string(page, lang=lang_code)
    return text

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
        fs = FileSystemStorage("static/contents")
        file.name = file.name.replace(" ","_")
        file.name = file.name.replace("&","_and_")
        filename = fs.save(file.name, file)
        uploaded_file_url = fs.url(filename)
        title = request.POST.get('title')
        subtitle = request.POST.get('subtitle')
        author = request.POST.get('author')
        subject = request.POST.get('subject')
        documentType = request.POST.get('docType')

        print(documentType)

        subject_code = re.search("\((.*)\)", subject).group(1)
    
        #request.build_absolute_uri('/')[:-1] + "/static/contents" +
        file_text = processPdf( fs.location + uploaded_file_url,"eng")
        fileUpload = FileUpload(title = title,subtitle=subtitle, author = author, subject=subject,documentType = documentType,file_text = file_text,file_location=request.build_absolute_uri('/')[:-1] + "/static/contents" + uploaded_file_url,file_size=longToSizeString(file.size),file_name=file.name,subject_code = subject_code)
        fileUpload.save()
        
        reply = {"success" : "file uploaded successfully","file-url": uploaded_file_url}
        return JsonResponse(reply)

    reply = {"error" : "No File Provided"}
    return JsonResponse(reply)




def advancedSearch(request):

    query = request.GET.get("query")
    files = []
    if query is not None:
        query_lower = query.lower()
        for obj in FileUpload.objects.all():
            if obj.title.lower().find(query_lower) != -1 or obj.subtitle.lower().find(query_lower) != -1 or obj.author.lower().find(query_lower) != -1 or obj.file_text.lower().find(query_lower) != -1:
                files.append(obj)
    jsonString = "["
    for file in files:
        jsonString += file.toStr().replace("'","\"")+","
    print(jsonString[-1])
    if jsonString[-1] == ',':
        jsonString = jsonString[:-1]
    jsonString += "]"


    return HttpResponse(jsonString)



def allDocs(request):
    res = []
    for obj in FileUpload.objects.all():
        res.append(str(obj.id) + "\t| " + obj.title + "\t| " + obj.author + "\t| " + obj.subject + "\t| " + obj.file_text + "\t| " + obj.file_location + "\t| " + obj.file_size +  "\t| " + str(obj.file_name) + "\t| " + obj.subject_code +"\t| " + obj.documentType + "<br><br><br><br>" )
    return HttpResponse(res)


def allVisit(request):
    res = []
    for obj in DocViews.objects.all():
        res.append(str(obj.id) + "\t| " + obj.username + "\t| " + str(obj.visit_id) + "<br><br><br><br>" )
    return HttpResponse(res)

def clear(request):
    for obj in DocViews.objects.all():
        obj.delete()
    for obj in FileUpload.objects.all():
        obj.delete()
    return HttpResponse("Success")


