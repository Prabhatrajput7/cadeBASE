from django.urls import path
from . import views

app_name ='user'

urlpatterns = [
    path('',views.dashboard,name='dashboard'),
    path('register/',views.register,name='register'),
    path('login/',views.loginform,name='login'),
    path('logout/',views.logout,name='logout'),
    path('forgotpassword/',views.forgotPassword,name='forgotPassword'),
    path('resetpassword/',views.resetPassword,name='resetPassword'),
    path('resetpassword/<uidb64>/<token>/',views.resetpasswordvalidate,name='resetpasswordverification'),
    path('activate/<uidb64>/<token>/',views.activate,name='activate'),
]

