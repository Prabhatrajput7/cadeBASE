from django.urls import path
from . import views

app_name ='cart'

urlpatterns = [
    path('',views.cartfx, name='cartfx'),
    path('add/<int:id>/', views.addtocart, name='addcart'),
    path('decrement/<int:id>/<int:cart_id>/', views.decrementfromcart, name='decrementcart'),
    path('remove/<int:id>/<int:cart_id>/', views.removefromcart, name='remove'),
    path('checkout', views.checkout, name='checkout'),
]