from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('product/', views.product, name='product'),
    # path('customer/', views.customer, name='customer'),
    path('customer/<int:pk>/', views.customer, name='customerdetail'),

    path('createorder/', views.createorder,name = 'createorder'),
    path('update/<int:pk>/',views.updateord ,name='updateorder'),
    path('delete/<int:pk>/',views.deleteord ,name='deleteorder'),

    path('creatcustomer/', views.creatcustomer,name = 'creatcustomer'),
    path('customer/<int:pk>/placeorder/', views.placecust,name = 'pcustomer'),
    path('customer/<int:pk>/updatecustomer/', views.updatecust,name = 'ucustomer'),
    path('customer/<int:pk>/deletecustomer/', views.deletecust,name = 'dcustomer'),
]
