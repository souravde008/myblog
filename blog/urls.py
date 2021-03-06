from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('admin/', include('admin.urls')),
    path('blog/', include('blogapp.urls')),
    path('',views.index),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
