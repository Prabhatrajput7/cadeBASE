from django import views
from django.urls import path
from . import views
urlpatterns = [
    path('',views.BCreate.as_view(), name='create'),
    path('thx/',views.Bthx.as_view(), name='thx'),
    path('book/',views.Bookk.as_view(), name='list'),
    path('book/<int:pk>/',views.Booktails.as_view(), name='display'),
    path('book/<pk>/delete/',views.BookDELETE.as_view(), name='delete'),
    path('book/<pk>/update/',views.Bookup.as_view(), name='update'),
]
