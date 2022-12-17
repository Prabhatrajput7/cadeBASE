from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('reviewView', views.ReviewModelVS, basename='ReviewViewSet')
router.register('streamplatform', views.SteamPlatform, basename='streamplatform')

app_name = 'app2'

urlpatterns = [
    path('stream/',views.Streamclass.as_view(),name='stream'),
    path('stream/<int:pk>',views.StreamclassPK.as_view(),name='streamplatform-detail'),
    path('watch/',views.Watchclass.as_view(),name='watch'),
    path('watch/<int:pk>',views.WatchclassPK.as_view(),name='watchlist-detail'),

    path('watch/<int:pk>/review/',views.ReviewListCreateAD.as_view(),name='review-create'),
    # create review for a movie without sending movie id and user id
    path('watch/<int:pk_alt>/review/<int:pk>',views.ReviewDetailAD.as_view(),name='review-detail'),
    # view individual review of any movie

    path('review/',views.ReviewList.as_view(),name='review'),
    path('review/<int:pk>',views.ReviewDetail.as_view(),name='reviewind-detail'),
    path('',include(router.urls)),

    # filter
    path('review/<str:username>',views.ReviewFilter.as_view(), name='review-filter'),
    path('reviewbyuser/',views.ReviewFilterQueryPara.as_view(), name='review-query'),

]
