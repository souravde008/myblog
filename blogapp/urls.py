from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('login/',views.login,name='login'),
    path('signup/', views.signup,name='signup'),
    path('logout/', views.logout, name='logout'),

    path('home/',views.home,name='home'),
    path('add-blog/',views.addBlog,name='add'),
    path('edit-blog/<int:id>',views.editBlog,name='edit'),
    path('update-blog/',views.updateBlog,name='update'),
    path('delete-blog/<int:id>',views.destroy,name='delete'),
    path('show-blog/<int:id>',views.showBlog,name='show'),

]