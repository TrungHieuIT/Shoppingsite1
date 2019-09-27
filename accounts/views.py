from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.shortcuts import render,redirect
from .forms import CustomerUserCreationForm 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login , logout ,authenticate
def SignUpView(request):
    if request.method == 'POST':
        form = CustomerUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('core:index')
    else:
        form = CustomerUserCreationForm()
    return render(request,'homepage/signup.html',{'form' : form})

def LoginView(request):
    if request.method =="POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('core:index')
    else:
        form = AuthenticationForm()
    return render(request,'homepage/login.html',{'form':form})    

def LogoutView(request):
    if request.method =="POST":
        logout(request)
        return redirect('core:index')