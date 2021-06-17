from django.shortcuts import render, redirect
from django.contrib.auth import logout as django_logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse , JsonResponse
from django.contrib.auth import authenticate, login
from . models import Users
from django.forms.models import model_to_dict
import json

from django.contrib.auth.hashers import make_password, check_password
# Create your views here.

#default page
def index(request):
    if request.session.get('user_id'):
        return redirect(home)
    return render(request,'index.html')

################Authentication#################
def login(request):
    if not request.session.get('user_id'):
        # print("Enter")
        if request.method == "POST":
            mail = request.POST.get('user_mail','')
            password = request.POST.get('user_password','')
            try:
                user = Users.objects.get(user_mail=mail)
            except:
                return HttpResponse("<h1>check email</h1>")

            if  check_password(password,user.user_password):
                request.session['user_id'] = user.pk
                return redirect('../home/')
            else:
                return HttpResponse("Not Done Here")
        return render(request, 'login.html')
    else:
        return redirect(home)
def signup(request):
    if not request.session.get('user_id'):
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
            user_password = make_password(user_password)
            user = Users(user_name=user_name,user_mail=user_mail,user_phone = user_phone,user_password=user_password)
            user.save()
            done = True
            request.session['user_id'] = user.pk
            return render(request,'signup.html',{'existuser':existuser,'passwordnotmatch':passwordnotmatch,'done':done})
        return render(request,'signup.html')
    else:
        return redirect(home)


def logout(request):
    try:
        del request.session['user_id']
        global ses
        ses = False
    except KeyError:
        pass
    return redirect('/')



################Content Page#################

def home(request):
    if request.session.get('user_id'):
        user= Users.objects.get(id = request.session['user_id'])
        user = user.user_name
        return render(request, 'home.html',{'user':user});
    return redirect('/')


def addBlog(request):
    pass

def editBlog(request):
    pass

def deleteBlog(request):
    pass