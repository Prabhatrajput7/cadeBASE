from django.urls import path

from app import views


urlpatterns = [
    # path('', views.multi, name='multi'),
    path('', views.FileFieldFormView.as_view(), name='multi2'),
    path('thx/', views.thx, name='thx'),
    path('list/', views.HuskyL.as_view(), name='list'),
]
