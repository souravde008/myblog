from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('login/',views.login,name='login'),
    path('signup/', views.signup,name='signup'),
    path('logout/', views.logout, name='logout'),

    path('home/',views.home,name='home'),
    path('add-blog/',views.addBlog,name='add'),
    path('edit-blog/',views.editBlog,name='edit'),
    path('delete-blog/',views.deleteBlog,name='delete'),
]