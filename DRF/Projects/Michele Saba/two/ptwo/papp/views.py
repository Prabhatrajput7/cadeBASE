from django.shortcuts import render
from rest_framework import generics, mixins, viewsets
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from .models import Profile, ProfileStatus
from .serializers import ProfileSerial, ProfileAvatarSerial, ProfileStatusSerial
from .permissions import IsOwnProfileOrReadOnly,IsOwnerOrReadOnly
# Create your views here.

# class ProfileList(generics.ListAPIView):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerial
#     permission_classes = [IsAuthenticated, DjangoModelPermissions]

# class ProfileViewList(ReadOnlyModelViewSet):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerial
#     permission_classes = [IsAuthenticated,IsOwnProfileOrReadOnly]

class ProfileViewList(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerial
    permission_classes = [IsAuthenticated,IsOwnProfileOrReadOnly]

class ProfileSSViewList(viewsets.ModelViewSet):
    serializer_class = ProfileStatusSerial
    permission_classes = [IsAuthenticated,IsOwnerOrReadOnly]   

    def get_queryset(self):
        queryset = ProfileStatus.objects.all()
        username = self.request.query_params.get("username", None)
        if username is not None:
            queryset = queryset.filter(user_profile__user__username=username)
        return queryset

    def perform_create(self, serializer):
        user_profile = self.request.user.profile
        serializer.save(user_profile=user_profile) 

class AvatarUpdateView(generics.UpdateAPIView):
    serializer_class = ProfileAvatarSerial
    permission_classes = [IsAuthenticated]

    def get_object(self):
        print('in')
        profile_object = self.request.user.profile
        return profile_object


"""
so that we can have an endpoint in the form of API is Avatar, where there is no need to pass any primary
key because we are going to use the get object method to automatically identify and return the profilings
that's associated with request user.
get_object returns an object (an instance of your model), while get_queryset returns a QuerySet object mapping to a set of potentially multiple instances of your model. In the case of the DetailView (or in fact any class that inherits from the SingleObjectMixin, the purpose of the get_queryset is to restrict the set of objects from which you'll try to fetch your instance.
"""