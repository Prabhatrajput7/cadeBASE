from django.urls import path
from . import views

urlpatterns = [
    path('',views.carhome, name='carhome'),
    path('about/',views.carabout, name='carabout'),
    path('services/',views.carservices, name='carservices'),
    path('contact/',views.carcontact, name='carcon'),

]
