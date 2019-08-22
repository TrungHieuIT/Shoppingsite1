from django.shortcuts import render
from django.views import View
from django.http import HttpResponse,HttpResponseRedirect
from .models import Product,Category

# Create your views here.

class HomeView(View):
    def get(self,request):
        listCategory = Category.objects.all()
        context = {'listscan' : listCategory}
        return render(request,'homepage/index.html', context=context)

def dangky(request):
    return render(request,'homepage/dangky.html')

def dangnhap(request):
    return render(request,'homepage/dangnhap.html')

def categories(request):
    listCategory = Category.objects.all()
    context = {'listscan' : listCategory}
    return render(request, 'homepage/navbar.html', context)

def laptop(request):
    return render(request,'homepage/laptop.html')