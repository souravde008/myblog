from django.urls import path
from . import views

urlpatterns = [
	path('',views.index, name="admin-index"),
	path('home/',views.home, name="admin-home"),
	path('logout/', views.logout, name = "admin-logout"),
	path('blogs/', views.blogs, name = "admin-blogs"),
	path('users/', views.users, name = "admin-users")
]