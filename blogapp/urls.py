from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
    path('home/',views.home),
    path('login/',views.login,name='login'),
    path('signup/', views.signup,name='signup'),
    path('logout/', views.logout, name='logout'),
]