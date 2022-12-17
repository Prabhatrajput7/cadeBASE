from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('hariorg',views.HariListV)


urlpatterns = [
    path('hhh/',views.harione),
    # path('hariemp/',views.hari_list),
    # path('hariemp/<int:pk>',views.hariemp_details)
    # path('hariemp/',views.HariList.as_view()),
    # path('hariemp/<int:pk>',views.Hariempdetails.as_view())
    path('harr/', include(router.urls))
]
