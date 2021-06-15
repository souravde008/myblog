from django.shortcuts import render, redirect
from django.contrib.auth import logout as django_logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse , JsonResponse
from django.contrib.auth import authenticate, login
from . models import Users
# Create your views here.


def index(request):
    return render(request,'index.html')


def login(request):
    email=""
    password = ""
    if request.user.is_authenticated:
        return render(request, 'home.html')
    if request.method == "POST":
        email = request.POST.get('email','')
        password = request.POST.get('password','')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'home.html')
        else:
            return HttpResponse("Not Done")
        
    return render(request, 'login.html')

def signup(request):
    existuser = False
    passwordnotmatch = False
    done = False
    if request.method == "POST":
        user_name = request.POST.get('user_name','')
        user_mail = request.POST.get('user_mail','')
        user_phone = request.POST.get('user_phone','')
        user_password = request.POST.get('user_password','')
        confirm_user_password = request.POST.get('confirm_user_password','')
        user = Users.objects.filter(user_mail=user_mail)
        if len(user) > 0:
            existuser = True
            print(existuser)
            return render(request,'signup.html',{'existuser':existuser,'passwordnotmatch':passwordnotmatch,'done':done})
        elif user_password != confirm_user_password:
            passwordnotmatch = True
            print(passwordnotmatch)
            return render(request,'signup.html',{'existuser':existuser,'passwordnotmatch':passwordnotmatch,'done':done})
        user = Users(user_name=user_name,user_mail=user_mail,user_phone = user_phone,user_password=user_password)
        user.save()
        done = True
        return render(request,'signup.html',{'existuser':existuser,'passwordnotmatch':passwordnotmatch,'done':done})
    return render(request,'signup.html')


@login_required
def logout(request):
    django_logout(request)
    return redirect('/')


def home(request):
    if request.user.is_authenticated:
        return render(request, 'home.html');
    return redirect('/')
