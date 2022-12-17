from django.urls import path
from . import views

urlpatterns = [
    path('',views.Fileup, name='File'),
    # path('',views.Fileimg.as_view(), name='File'),
    path('thx/',views.Thx.as_view(), name='thx')
]
