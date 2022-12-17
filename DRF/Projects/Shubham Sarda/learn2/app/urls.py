from django.urls import path
from . import views


""""
usemy
"""
urlpatterns = [
    # path('',views.MovieNS, name='firstfx'),
    path('',views.Movieclass.as_view(), name='firstclass'),
    # path('<int:pk>',views.MoviePK, name='firstpkfx'),
    path('<int:pk>',views.MovieclassPK.as_view(), name='movie-detail')
    # name='movie-detail' to work with hyperlink seriliers modelname-detail
]
