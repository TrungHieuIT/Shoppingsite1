from django.shortcuts import render
from django.views import View
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.

class HomeView(View):
    def get(self,request):
        return render(request,'homepage/index.html')

def dangky(request):
    return render(request,'homepage/dangky.html')

def dangnhap(request):
    return render(request,'homepage/dangnhap.html')

