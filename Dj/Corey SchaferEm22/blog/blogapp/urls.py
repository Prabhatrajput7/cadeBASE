from django.urls import path
from . import views

app_name ='blogapp'

urlpatterns = [
    path('',views.BlogList.as_view(), name='home'),
    path('user/<str:username>',views.UserPostListView.as_view(), name='ussr'),
    path('post/<int:pk>',views.BlogDetailView.as_view(), name='detail'),
    path('post/ucomment/<int:pk>',views.BlogDetailView.as_view(), name='upcom'),
    path('post/dcomment/<int:pk>',views.dcomment, name='delcom'),
    path('post/new',views.BlogCreateView.as_view(), name='create'),
    path('post/<int:pk>/update',views.BlogUpdateView.as_view(), name='update'),
    path('post/<int:pk>/delete',views.BlogDeleteView.as_view(), name='delete'),
    path('about/',views.about, name= 'about'),
]
