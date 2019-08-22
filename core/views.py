from django.shortcuts import render
from django.views import View
from django.http import HttpResponse,HttpResponseRedirect
from .models import Product,Category,Brand,Cart,Order,Variation,User

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
    listCategory = Category.objects.all()
    productcate = Product.objects.filter(pro_id = id)
    detail = Product.objects.get(pro_id = id)
    detailBrand = Brand.objects.all()
    context = {'productcate' : productcate,'listscan' :listCategory,'detail' :detail ,'detailBrand' :detailBrand }

    return render(request,'homepage/chiTietSanPham.html',context=context)


def productCate(request,id):
    listCategory = Category.objects.all()
    productcate = Product.objects.filter(cate_id = id)
    context = {'productcate' : productcate ,'listscan' :listCategory}
    return render(request,'homepage/sanPhamDanhMuc.html',context)