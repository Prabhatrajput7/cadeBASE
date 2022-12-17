from django.urls import path
from . import views

urlpatterns = [
    path('',views.allattack,name='all'),
    path('<int:pk>/',views.individual,name='individual'),
]
