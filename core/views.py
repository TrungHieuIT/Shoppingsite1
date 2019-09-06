from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from .models import Product,Category,Brand
from cart.forms import CartAddProductForm
# Create your views here.

#class HomeView(View):
    #def get(self,request):
        #list = Product.objects.all().order_by('-pro_id')
        #listCategory = Category.objects.all()
        #brand = Brand.objects.all()
        #context = {'listscan' : listCategory,'listProduct' : list,'brand':brand}
        #return render(request,'homepage/index.html', context=context)

   
    
    
    
#def quickView(request,id):
    #listCategory = Category.objects.all()
    #productcate = Product.objects.filter(pro_id = id)
    #detail = Product.objects.get(pro_id = id)
    #detailBrand = Brand.objects.all()
    #otherPro = Product.objects.filter(cate_id = detail.cate_id)
    #context = {'productcate' : productcate,'listscan' :listCategory,'detail' :detail ,'detailBrand' :detailBrand ,'otherPro':otherPro}
    #return render(request,'homepage/quickView.html',context=context)

#def dangky(request):
    #return render(request,'homepage/dangky.html')

#def dangnhap(request):
    #return render(request,'homepage/dangnhap.html')

#def cart(request):
    #return render(request,'homepage/giohang.html')

def chiTietSanPham(request,id):
    listCategory = Category.objects.all()
    productcate = Product.objects.filter(id = id)
    detail = Product.objects.get(id = id)
    brand = Brand.objects.all()
    otherPro = Product.objects.filter(cate_id = detail.cate_id)
    product = get_object_or_404(Product,id = id , status = True)
    cart_product_form = CartAddProductForm()
    context = {'productcate' : productcate,
                'listscan' :listCategory,
                'detail' :detail ,
                'brand' : brand ,
                'otherPro':otherPro,
                'product' : product,
                'cart_product_form': cart_product_form,
                }
    return render(request,'homepage/chiTietSanPham.html',context=context)

def index (request,category_slug = None):
       category = None
       categories = Category.objects.all()
       brand = Brand.objects.all()
       products = Product.objects.all().order_by('-id')
       if category_slug:
           category = get_object_or_404(Category,slug=category_slug)
           products = Product.objects.filter(category=category)
       
       context ={
           'listscan': categories,
           'category' : category,
           'products' : products,
           'brand' : brand,
        }
       return render(request,'homepage/index.html',context = context)