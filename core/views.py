from django.shortcuts import render
from django.views import View
from django.http import HttpResponse,HttpResponseRedirect
from .models import Product,Category

# Create your views here.

class HomeView(View):
    def get(self,request):
        list = Product.objects.all().order_by('-pro_id')
        listCategory = Category.objects.all()
        context = {'listscan' : listCategory,'listProduct' : list}
        return render(request,'homepage/index.html', context=context)
    
    


def dangky(request):
    return render(request,'homepage/dangky.html')

def dangnhap(request):
    return render(request,'homepage/dangnhap.html')
def chiTiet(request,id):
    productcate = Product.objects.filter(pro_id = id)
    context = {'productcate' : productcate }
    return render(request,'homepage/chiTietSanPham.html')

def productCate(request,id):
    listCategory = Category.objects.all()
    productcate = Product.objects.filter(cate_id = id)
    context = {'productcate' : productcate ,'listscan' :listCategory}
    return render(request,'homepage/sanPhamDanhMuc.html',context)