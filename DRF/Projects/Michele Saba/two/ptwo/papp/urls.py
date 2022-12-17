from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register("profiles", views.ProfileViewList)
router.register("profilesSS", views.ProfileSSViewList,basename='status')

# profile_list = views.ProfileViewList.as_view({'get','list'})
# profile_detail = views.ProfileViewList.as_view({'get','retrieve'})

urlpatterns = [
    # path("profiles/", views.ProfileList.as_view(), name='ListingProfile' ),
    path("", include(router.urls)),
    path("avatar/", views.AvatarUpdateView.as_view(), name="avatar-update"),
    
    # path("profiles/", profile_list, name='viewlist'),
    # path("profiles/<int:pk>", profile_detail, name='viewdetail'),
]
