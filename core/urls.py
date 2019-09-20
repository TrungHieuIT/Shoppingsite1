from django.urls import path
from .views import SearchResultsView
from . import views 

app_name ='core'
urlpatterns = [
    #path('', HomeView.as_view(), name ='index'),
    #path('dangky/',views.dangky,name="dang ky"),
    #path('dangnhap/',views.dangnhap,name="dang nhap"),
    #path('giohang/',views.cart,name="gio hang"),
    #path('quickView/<int:id>/',views.quickView,name="xem nhanh"),
    #path('chiTietSanPham/<int:id>/',views.detail,name="chi tiet san pham"),
    path('sanpham/<int:id>/',views.productCate,name="san pham thuoc danh muc "),
    path('',views.index ,name='index'),
    path('chiTietSanPham/<int:id>/',views.chiTietSanPham,name="chi-tiet-san-pham"),
    path('upvote/<int:id>',views.upvote, name ='up vote'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    
]