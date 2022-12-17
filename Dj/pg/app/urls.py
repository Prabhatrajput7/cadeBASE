from django.urls import path

from app.models import R6
from . import views

urlpatterns = [
    path('product/', views.subdomaincheck, name='subdomain'),
    path('siege/', views.siege, name ='siege'),
    path('siege/<str:id>', views.siegeid, name ='siegeid'),
    path('raw/', views.raw),
    path('rawsql/', views.rawsql),
    path('classr6/', views.Siege.as_view(),name ='csiege')
]
