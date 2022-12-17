"""ptwo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token


from dj_rest_auth.views import (
    LoginView, LogoutView, PasswordChangeView, PasswordResetConfirmView,
    PasswordResetView, UserDetailsView,
)
from django.views.decorators.csrf import csrf_exempt
from dj_rest_auth.registration.views import RegisterView, VerifyEmailView, ResendEmailVerificationView
# "C:\Users\Prabh\AppData\Local\Programs\Python\Python310\lib\site-packages\rest_auth\urls.py"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('papp.urls')),
    path("api-auth/", include("rest_framework.urls")),
    # path("api/rest-auth/", include("dj_rest_auth.urls")),
    # path("api/rest-auth/registration/", include("dj_rest_auth.registration.urls")),

    # path("registration/", include("dj_rest_auth.registration.urls")), working

    # old
    # path('api/rest-auth/',include("rest_auth.urls")),
    # path("api/rest-auth/registration/", include("rest_auth.registration.urls"))
    # path('api-token-auth/',obtain_auth_token,name='api-token-auth'),


    # path('password-reset/', PasswordResetView.as_view(),),
    # path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('login/', LoginView.as_view(), name='rest_login'),
    # URLs that require a user to be logged in with a valid session / token.
    # path('logout/', LogoutView.as_view(), name='rest_logout'),
    # path('user/', UserDetailsView.as_view(), name='rest_user_details'),
    # path('password/change/', PasswordChangeView.as_view(), name='rest_password_change'),
    

    # path('register/', RegisterView.as_view(), name='rest_register'),
    # path('verify-email/', VerifyEmailView.as_view(), name='rest_verify_email'),
    # path('resend-email/', ResendEmailVerificationView.as_view(), name="rest_resend_email"),
]

from django.conf.urls.static import static
from django.conf import settings

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
