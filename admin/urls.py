from django.urls import path
from . import views

urlpatterns = [
	path('',views.index, name="admin-index"),
	path('home/',views.home, name="admin-home"),
	path('logout/', views.logout, name = "admin-logout")
]