from django.shortcuts import render, redirect
from django.http import HttpResponse , JsonResponse
from . backends import AuthBackend
from blogapp.models import Users, Blogs
# Create your views here.
def index(request):
	if not request.session.get('admin_id'):
		if request.method == 'POST':
			username = request.POST.get('username')
			password = request.POST.get('password')
			user = AuthBackend.authenticate(request,username=username, password=password)
			# print(user.user_name)
			# exit()
			if user is not None:
				if user.is_admin:
					request.session['admin_id'] = user.pk
					return redirect("admin-home")
		return render(request, 'a_login.html')
	return redirect("admin-home")


def logout(request):
    try:
        del request.session['admin_id']
        
    except KeyError:
        pass
    return redirect('admin-index')



def home(request):
	if request.session.get('admin_id'):
		blogs = Blogs.objects.all()
		users = []
		for blog in blogs:
			ids = blog.user_id
			# print(ids)
			user = Users.objects.filter(id = ids)
			for usr in user:
				users.append(usr.user_name)

		# print(users)
		alldata = zip(blogs,users)
		return render(request,'a_home.html',{'alldata':alldata})
	return redirect("admin-index")
