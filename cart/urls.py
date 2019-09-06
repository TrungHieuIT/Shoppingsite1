from django.urls import path
from django.conf.urls import url
from . import views

app_name ='cart'

urlpatterns = [
    #url(r'^$',views.cart_detail ,name='cart_detail'),
    #url(r'^add/(?P<product_id>\d+)/$', views.cart_add, name='cart_add'),
    #url(r'^remove/(?P<product_id>\d+)/$',views.cart_remove,name='cart_remove'),
    path('',views.cart_detail,name ='cart_detail'),
    path('add/<int:id>/',views.cart_add,name='cart_add'),
    path('remove/<int:id>/',views.cart_remove, name='cart_remove'),
]