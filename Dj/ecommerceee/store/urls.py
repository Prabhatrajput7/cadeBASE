from django.urls import path
from . import views

app_name ='store'

urlpatterns = [
    path('',views.storefx, name='storefx'),
    path('category/<slug:slugcat>/',views.storefx, name='storedcat'),
    path('<slug:slugcat>/<slug:slugpro>/',views.productdetfx, name='storedpro'),
    path('search/', views.searching, name = 'search')
]
