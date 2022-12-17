from argparse import Namespace
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('all', views.Modelallj)

urlpatterns = [
    path('model/', include(router.urls)),
    path('', include('userd.urls')),
    path('alljd/',views.AllJD.as_view()),
    path('alljd/<int:pk>',views.Jdetail.as_view()),
    path('alljd/apply/<int:pk>',views.JAdetail.as_view()),
]