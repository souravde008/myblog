from django.shortcuts import render, redirect
from django.http import HttpResponse , JsonResponse
from . backends import AuthBackend
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
	else:
		return redirect("admin-home")
	return render(request, 'login.html')
def home(request):
	return render(request,'home.html')
