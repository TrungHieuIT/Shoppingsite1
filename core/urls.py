from django.urls import path
from .views import HomeView
from . import views
urlpatterns = [
    path('', HomeView.as_view(), name ='index'),
    path('dangky/',views.dangky,name="dang ky"),
    path('dangnhap/',views.dangnhap,name="dang nhap"),
    path('giohang/',views.cart,name="gio hang"),
    path('chiTietSanPham/<int:id>/',views.detail,name="chi tiet san pham"),
    path('sanpham/<int:id>/',views.productCate,name="san pham thuoc danh muc "),

]