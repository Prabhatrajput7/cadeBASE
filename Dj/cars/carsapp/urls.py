from django.urls import path
from . import views

urlpatterns = [
    path('',views.carcars, name='carcar'),
    path('car/<str:id>',views.car_detail, name='car_detail'),
    path('search/', views.search, name='search'),
]
