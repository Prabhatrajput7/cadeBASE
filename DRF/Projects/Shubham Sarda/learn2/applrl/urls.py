from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

"""
acess token is for 5 mins valide and refrest is for 24 hrs
"""

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)


urlpatterns = [
    path('login/', obtain_auth_token, name='login'),
    path('register/', views.registration_view, name='register'),
    path('logout/', views.logout_view, name='logout'),

    # path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair') working ,
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]