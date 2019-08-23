from django.shortcuts import render,redirect
from .forms import RegisterForm
from django.http import HttpResponseRedirect
#from django.contrib.auth.models import User , auth 
# Create your views here.


def dangky(request):
    form = RegisterForm()
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'homepage/dangky.html', {'form':form})
def dangnhap(request):
    return render(request, 'homepage/dangnhap.html')