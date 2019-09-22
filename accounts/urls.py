from django.urls import path
from .import views
from django.views.generic.base import TemplateView
urlpatterns = [
    path('signup/', views.SignUpView, name='signup'),
    path('login/',views.LoginView,name="login"),
    path('logout/',views.LogoutView,name="logout"),
]
