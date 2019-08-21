from django.urls import path
from .views import HomeView
from . import views
urlpatterns = [
    path('', HomeView.as_view(), name ='index'),
    path('dangky/',views.dangky,name="dang ky"),
    path('dangnhap/',views.dangnhap,name="dang nhap"),
    path('laptop/1',views.laptop,name="laptop"),
]