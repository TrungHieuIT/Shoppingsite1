from django.urls import path
from django.conf.urls import url
#from .views import HomeView
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
]