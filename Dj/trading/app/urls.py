from django.urls import path
from . import views

urlpatterns = [
    path('',views.stockerp, name='stockerp'),
    path('stocktracker/',views.stockert, name='stocktra'),
]


# code keen
# path('api/order/',views.stockerp, name='post'),