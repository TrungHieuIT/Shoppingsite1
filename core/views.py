from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import Product,Category,Brand
from cart.forms import CartAddProductForm
from django.views.generic.list import ListView
from django.db.models import Q

from django.contrib.postgres.search import SearchQuery, SearchRank,SearchVector
# Create your views here.

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
       products_vote = Product.objects.filter().order_by('-vote')
       if category_slug:
           category = get_object_or_404(Category,slug=category_slug)
           products = Product.objects.filter(category=category)

       
       context ={
           'listscan': categories,
           'category' : category,
           'products' : products,
           'brand' : brand,
           'vote' : products_vote,
        }
       return render(request,'homepage/index.html',context = context)

def productCate (request,id):
    listCategory = Category.objects.all()
    productcate = Product.objects.filter(cate_id = id)
    context ={
        'productcate' : productcate,
        'listscan' : listCategory,
    }
    return render(request,'homepage/sanPhamDanhMuc.html',context)

def upvote (request , id):
    productVote = Product.objects.get(id = id )
    productVote.vote +=1
    productVote.save()
    return redirect('core:index')

class SearchResultsView(ListView):
    model = Product
    template_name ='homepage/search.html'
    
    def get_queryset(self):
        query = self.request.GET.get('search')
        object_list = Product.objects.filter(
            Q(pro_name__icontains = query) | Q(price__icontains = query ) | Q(pro_year__icontains = query) | Q(slug__icontains = query)
        )
        return object_list
        

    