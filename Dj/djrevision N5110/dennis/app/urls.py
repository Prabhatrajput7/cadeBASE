import imp
from . import views
from django.urls import path
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/',views.CustomLogin.as_view(),name='login'),
    path('register/',views.RegisterNow.as_view(),name='register'),
    path('logout/',LogoutView.as_view(next_page = 'login'),name='logout'),
    path('reset_password',auth_views.PasswordResetView.as_view(template_name='app/password_reset.html'),name='reset_password'),
    path('reset_password_sent',auth_views.PasswordResetDoneView.as_view(template_name='app/password_reset_sent.html'),name='password_reset_done'),
    path('reset<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(template_name='app/password_reset_con.html'),name='password_reset_confirm'),
    path('reset_password_complete',auth_views.PasswordResetCompleteView.as_view(template_name='app/password_reset_comp.html'),name='password_reset_complete'),
    path('',views.TaskList.as_view(),name='list'),
    path('all/',views.Tall.as_view(),name='all'),
    path('create/',views.TCreate.as_view(),name='create'),
    path('update/<int:pk>',views.Tupdate.as_view(),name='up'),
    path('delete/<int:pk>',views.TDelete.as_view(),name='del'),
    path('task/<int:pk>',views.TaskDetail.as_view(),name='detail'),
]
