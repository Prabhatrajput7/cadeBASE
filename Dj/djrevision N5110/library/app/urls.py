from django.urls import path
from . import views

urlpatterns = [
    path('',views.HomeCount.as_view(),name='list'),
    path('listbook/',views.ListBook.as_view(),name='listallbook'),
    path('book_detail/<int:pk>',views.Book_detail.as_view(),name='book_detail'),
    path('addbook/',views.BBK.as_view(),name='book'),
    path('thankks/',views.thx,name='thx'),
    path('logreq/',views.logreq,name='logreq'),
    path('signup/',views.SignUpView.as_view(),name='Signup'),
    path('profile/',views.CheckedOutBooksByUserView.as_view(),name='profile'),
]
