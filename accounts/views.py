from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.shortcuts import render,redirect
#from .forms import CustomerUserCreationForm 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login , logout
def SignUpView(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_vaild():
            user = form.save()
            login(request,user)
            return redirect('core:index')
    else:
        form = UserCreationForm()
    return render(request,'homepage/signup.html',{'form' : form})

def LoginView(request):
    if request.method =="POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user =form.get_user()
            login(request,user)
            return redirect('core:index')
    else:
        form = AuthenticationForm()
    return render(request,'homepage/login.html',{'form':form})    

def LogoutView(request):
    if request.method =="POST":
        logout(request)
        return redirect('core:index')