from django.shortcuts import render, redirect
from django.contrib.auth import logout as django_logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse , JsonResponse
from django.contrib.auth import authenticate, login
from . models import Users
from django.forms.models import model_to_dict
import json

from django.contrib.auth.hashers import make_password
# Create your views here.


def index(request):
    return render(request,'index.html')


def login(request):
    if request.method == "POST":
        mail = request.POST.get('user_mail','')
        password = request.POST.get('user_password','')
        user = Users.objects.get(user_mail=mail)
        if user.user_password == password:
            request.session['user_id'] = user.pk
            return redirect('../home/',{'user_id':request.session['user_id']})
        else:
            return HttpResponse("Not Done Here")
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
            # print(existuser)
            return render(request,'signup.html',{'existuser':existuser,'passwordnotmatch':passwordnotmatch,'done':done})
        elif user_password != confirm_user_password:
            passwordnotmatch = True
            # print(passwordnotmatch)
            return render(request,'signup.html',{'existuser':existuser,'passwordnotmatch':passwordnotmatch,'done':done})
        
        user = Users(user_name=user_name,user_mail=user_mail,user_phone = user_phone,user_password=user_password)
        user.save()
        done = True
        return render(request,'signup.html',{'existuser':existuser,'passwordnotmatch':passwordnotmatch,'done':done})
    return render(request,'signup.html')


def logout(request):
    
    try:
        del request.session['user_id']
    except KeyError:
        pass
    return redirect('/')


def home(request):
    return render(request, 'home.html');
