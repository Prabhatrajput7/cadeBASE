from django.shortcuts import render
from rest_framework.views import APIView
from django.http import Http404
from app2.serializers import WatchListSerialz,StreamSerialz,ReviewSerializerz,ReviewSerializerzMVS
from app2.models import StreamPlatform,WatchList,Review
from rest_framework import status, permissions
from app2.permissions import IsOwnProfileOrReadOnly,IsAdminOrReadOnly
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle, ScopedRateThrottle
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins
from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from app2.throttling import ReviewCreateThrottle,ReviewListThrottle
from rest_framework import filters
from app2.pagination import PaginationNum,PaginationLimit,PaginationCursor

"""filter is can also be work with generic api view"""

class ReviewFilter(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializerz
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['review_user__username', 'watchlist']
    # filter_backends =[filters.SearchFilter]
    # search_fields = ['id']
    # filter_backends =[filters.OrderingFilter]
    # ordering_fields = ['rating']

    def get_queryset(self):
        username = self.kwargs['username']
        return Review.objects.filter(review_user__username=username)

class ReviewFilterQueryPara(generics.ListAPIView):
    # http://127.0.0.1:8000/app2/reviewbyuser/?username=usemy
    queryset = Review.objects.all()
    serializer_class = ReviewSerializerz

    def get_queryset(self):
        username = self.request.query_params.get("username", None)
        if username is not None:
            return Review.objects.filter(review_user__username=username)
        raise Http404

"""Model viewsEt"""

class SteamPlatform(viewsets.ModelViewSet):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamSerialz
    permission_classes = [permissions.IsAuthenticated]

class ReviewModelVS(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializerz
    permission_classes = [permissions.IsAuthenticated,IsOwnProfileOrReadOnly]
    pagination_class = PaginationCursor
    # throttle_classes = [ScopedRateThrottle]
    # throttle_scope = 'customscope'

    def perform_create(self, serializer):
        review_user = self.request.user
        serializer.save(review_user=review_user)

"""viewset"""
class ReviewViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    def list(self, request):
        queryset = Review.objects.all()
        serializer = ReviewSerializerz(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        rev = get_object_or_404(Review, pk=pk)
        serializer = ReviewSerializerz(rev)
        return Response(serializer.data)

"""Concrete"""

class ReviewListCreateAD(generics.ListCreateAPIView, generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated,IsOwnProfileOrReadOnly]
    serializer_class = ReviewSerializerzMVS
    # throttle_classes = [UserRateThrottle,AnonRateThrottle]

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(watchlist=pk)

    def check_user(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(watchlist=pk,review_user=self.request.user)

    def perform_create(self, serializer):
        if self.check_user().exists():
            raise ValidationError('You have already commented for this post :)')
        else:
            pk = self.kwargs.get('pk')
            watchlist = WatchList.objects.get(pk=pk)
            if watchlist.number_rating == 0:
                watchlist.avg_rating = serializer.validated_data['rating']
            else:
                watchlist.avg_rating = (watchlist.avg_rating + serializer.validated_data['rating'])/2
            watchlist.number_rating = watchlist.number_rating + 1
            watchlist.save()
            review_user = self.request.user
            serializer.save(watchlist=watchlist, review_user=review_user)

class ReviewDetailAD(generics.RetrieveUpdateDestroyAPIView, generics.GenericAPIView):

    permission_classes = [permissions.IsAuthenticated,IsOwnProfileOrReadOnly]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializerzMVS

    def get(self, request, *args, **kwargs):    
        pk = self.kwargs.get('pk_alt', '')
        pk2 = self.kwargs['pk']
        try:
            p_k = Review.objects.filter(watchlist=pk).get(id=pk2)
            sq = ReviewSerializerzMVS(p_k)
            return Response(sq.data)
        except Review.DoesNotExist:
            raise Http404
    
    def perform_update(self, serializer):
        pk = self.kwargs.get('pk_alt', '')
        watchlist = WatchList.objects.get(pk=pk)
        if watchlist.number_rating == 0:
            watchlist.avg_rating = serializer.validated_data['rating']
        else:
            watchlist.avg_rating = (watchlist.avg_rating + serializer.validated_data['rating'])/2
        watchlist.number_rating = watchlist.number_rating + 1
        watchlist.save()
        review_user = self.request.user
        serializer.save(watchlist=watchlist, review_user=review_user)
            

"""MiXINS"""

class ReviewDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializerzMVS

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

class ReviewList(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializerzMVS

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

"""API View"""




class Streamclass(APIView):

    permission_classes = [permissions.IsAuthenticated]
    
    def get(self,request):
        mov = StreamPlatform.objects.all()
        ser = StreamSerialz(mov, many=True, context={'request': request})
        """context={'request': request} for hyperlink only"""
        return Response(ser.data, status = status.HTTP_200_OK)

    def post(self,request):
        ser = StreamSerialz(data= request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status = status.HTTP_201_CREATED)
        return Response(ser.errors)

class Watchclass(APIView):

    permission_classes = [permissions.IsAuthenticated]
    
    def get(self,request):
        mov = WatchList.objects.all()
        ser = WatchListSerialz(mov, many=True, context={'request': request})
        return Response(ser.data, status = status.HTTP_200_OK)

    def post(self,request):
        ser = WatchListSerialz(data= request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status = status.HTTP_201_CREATED)
        return Response(ser.errors)        

class StreamclassPK(APIView):

    permission_classes = [permissions.IsAuthenticated]
    
    def getting(self,pk):
        try:
            one = StreamPlatform.objects.get(id=pk)
            return one
        except:
            raise Http404

    def get(self,request,pk):
        one = self.getting(pk)
        ser = StreamSerialz(one,context={'request': request})
        return Response(ser.data, status = status.HTTP_201_CREATED)

    def put(self,request,pk):
        one = self.getting(pk)
        ser = StreamSerialz(one, data= request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status = status.HTTP_201_CREATED)
        return Response(ser.data, status = status.HTTP_400_BAD_REQUEST)

    def patch(self,request,pk):
        one = self.getting(pk)
        ser = StreamSerialz(one, data= request.data, partial=True)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status = status.HTTP_201_CREATED)
        return Response(ser.data, status = status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        one = self.getting(pk)
        one.delete()
        return Response(status = status.HTTP_204_NO_CONTENT) 


class WatchclassPK(APIView):

    permission_classes = [permissions.IsAuthenticated]
    
    def getting(self,pk):
        try:
            one = WatchList.objects.get(id=pk)
            return one
        except:
            raise Http404

    def get(self,request,pk):
        one = self.getting(pk)
        ser = WatchListSerialz(one,context={'request': request})
        return Response(ser.data, status = status.HTTP_200_OK)

    def put(self,request,pk):
        one = self.getting(pk)
        ser = WatchListSerialz(one, data= request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status = status.HTTP_201_CREATED)
        return Response(ser.data, status = status.HTTP_400_BAD_REQUEST)

    def patch(self,request,pk):
        one = self.getting(pk)
        ser = WatchListSerialz(one, data= request.data, partial=True)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status = status.HTTP_201_CREATED)
        return Response(ser.data, status = status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        one = self.getting(pk)
        one.delete()
        return Response(status = status.HTTP_204_NO_CONTENT) 