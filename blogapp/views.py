from django.shortcuts import render, redirect
from django.contrib.auth import logout as django_logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse , JsonResponse
from django.contrib.auth import authenticate, login
from . models import Users, Blogs
from django.forms.models import model_to_dict
import json
from django.core.files.storage import FileSystemStorage

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
        try:
            users = Blogs.objects.filter(user_id = request.session['user_id'])
            name  = Users.objects.get(id = request.session['user_id'])

        except:
            return HttpResponse("Problem in id")
        if len(users)>0:
            return render(request, 'home.html',{'users':users,'user_name':name.user_name});
        else:
             return render(request, 'home.html',{'user_name':name.user_name});
    return redirect('/')


def addBlog(request):
    done = False
    if request.session.get('user_id'):
        user =  Users.objects.get(id = request.session.get('user_id'))
        if request.method == 'POST':
            blog_title = request.POST.get('blog_title','')
            try:
                img = request.FILES['imgfile']
            except:
                return HttpResponse("<h1>Reupload image</h1>")
            fs = FileSystemStorage()
            filename = fs.save(img.name, img)
            uploaded_file_url = fs.url(filename)
            blog_created_at = request.POST.get('blog_created_at','')
            blog_desc = request.POST.get('blog_desc','')
            print(user.id)
            blog = Blogs(user_id=user.id,blog_title=blog_title,blog_img=img,blog_created_at=blog_created_at,blog_desc=blog_desc)
            blog.save()
            done = True
            print(done)
            return render(request,'addBlog.html',{'done':done})
        return render(request,'addBlog.html')
    return redirect('/')


def editBlog(request,id):
    if request.session.get('user_id'):
        blog = Blogs.objects.get(id=id)
        return render(request,'editBlog.html',{'blog':blog})
    return redirect('/')

def updateBlog(request):
    if request.session.get('user_id'):
        if request.method == 'POST':
            blog = Blogs.objects.get(id=request.POST.get('id'))
            if blog == None:
                return HttpResponse('<h2>Blog Not Found</h2>')
            else:
                if request.FILES.get('imgfile') != None:
                    img = request.FILES['imgfile']
                    fs = FileSystemStorage()
                    uploaded_file_url = fs.save(img.name, img)
                else:
                    uploaded_file_url = None

                if uploaded_file_url != None:
                    blog.blog_img = uploaded_file_url
                    print(blog.blog_img)
                blog.blog_title = request.POST.get('blog_title')
                blog.blog_desc = request.POST.get('blog_desc')
                blog.blog_created_at= request.POST.get('blog_created_at')
                blog.save()
        return render(request,'editBlog.html')


def destroy(request,id):
    blog = Blogs.objects.get(id=id)
    blog.delete()
    return redirect("home")

def showBlog(request,id):
    blog = Blogs.objects.get(id=id)
    return render(request,'showBlog.html',{'blog':blog})