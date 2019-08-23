from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('register/',views.dangky,name="dang ky"),
    path('login/',views.dangnhap,name="dang nhap"),
    
]