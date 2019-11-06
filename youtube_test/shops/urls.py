from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.index,name='index'),
    path(r'shop_map', views.shop_map,name='shop_map'),
    path(r'base_layout',views.base_layout,name='base_layout'),
    path(r'getdata',views.getdata,name='getdata')
]