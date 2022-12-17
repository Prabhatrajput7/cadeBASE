"""cars URL Configuration

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


# https://github.com/dev-rathankumar/carzone-gitproject


from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from account.views import register,dashboard

# when you are using login with google or facebook make user it is localhost:8000
# python manage.py dumpdata --natural-foreign --natural-primary -e contenttypes -e auth.Permission --indent 4 > project_dump.json

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('carhome.urls')),
    path('cars/',include('carsapp.urls')),
    path('account/',include('account.urls')),
    path('contact/',include('contact.urls')),
    # path('socialaccounts/', include('allauth.urls')),

    # path('register/', register, name='register'),
    # path('dashboard/', dashboard, name='dashboard'),
    # path('accounts/login/', auth_views.LoginView.as_view(template_name='account/login.html'), name='login'),
    # path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),

]


from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)