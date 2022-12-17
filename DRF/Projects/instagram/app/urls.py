from django.urls import path, include
from . import views


urlpatterns = [
    path('api/',views.PostList.as_view()),
    path('api/<int:pk>',views.SinglePost.as_view()),
    path('vote/<int:pk>',views.Voter.as_view()),
    path('comment/<int:pk>',views.Comments.as_view(),name='comment-det'),
    # path('comment/<int:pk>/<int:pk1>',views.Commentsdel.as_view()),
    path('combyuser/<int:pk>',views.CommbyUser.as_view(),name='user-comm'),
    path('api-auth',include('rest_framework.urls'))
]
