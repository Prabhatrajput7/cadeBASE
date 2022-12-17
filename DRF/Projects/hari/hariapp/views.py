import imp
from django.http import Http404
from django.shortcuts import render
from django.http import JsonResponse
from .models import HariOne
from .serializers import HariSerializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import generics,mixins

from hariapp import serializers
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
# Create your views here.

#fx base views

def harione(request):
    data ={
        'alphaa':"A",
        'abphab':"B"
    }

    obj = HariOne.objects.all()
    enames = {'emp_name':list(obj.values('name','salary'))}

    return JsonResponse(enames)
    # return Response({'message':'hi'})
"""
@api_view(['GET','POST'])
def hari_list(request):
    if request.method == 'GET':
        hari = HariOne.objects.all()
        serial = HariSerializers(hari, many=True) #this many tells that its a list 
        return Response(serial.data)

    elif request.method == 'POST':
        serial = HariSerializers(data=request.data) #deserialization
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def hariemp_details(request,pk):
    try:
        emp_details = HariOne.objects.get(pk=pk)
    except HariOne.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        serial = HariSerializers(emp_details)
        return Response(serial.data)

    elif request.method == 'PUT':
        serial = HariSerializers(emp_details,data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        emp_details.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
"""

# classbase view
"""
class HariList(APIView):
    def get(self, request):
        hari = HariOne.objects.all()
        serial = HariSerializers(hari, many=True) #this many tells that its a list 
        return Response(serial.data)
    
    def post(self, request):
        serial = HariSerializers(data=request.data) #deserialization
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors,status=status.HTTP_400_BAD_REQUEST)


class Hariempdetails(APIView):
    def get_object(self,pk):
        try:
            return HariOne.objects.get(pk=pk)
        except HariOne.DoesNotExist:
            raise Http404

    def get(self,request,pk):
        emp_details = self.get_object(pk)
        serial = HariSerializers(emp_details)
        return Response(serial.data)

    def put(self, request,pk):#update
        emp_details = self.get_object(pk)
        serial = HariSerializers(emp_details,data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        emp_details = self.get_object(pk)
        emp_details.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
"""

# MIXIN do not repeat yourself DRY principle
# Mixin bunch of class | get post are handler methed
"""
class HariList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    # list this data, #post the data,#all generic based operations
    queryset = HariOne.objects.all()
    serializer_class = HariSerializers

    def get(self,request):
        return self.list(request)

    def post(self,request):
        return self.create(request)
    #note .list and .create are the methid inherited by listmix and create mix

class Hariempdetails(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin ,generics.GenericAPIView):
    queryset = HariOne.objects.all()
    serializer_class = HariSerializers

    def get(self,request,pk):
        return self.retrieve(request,pk)
    
    def put(self,request,pk):
        return self.update(request,pk)

    def delete(self,request,pk):
        return self.destroy(request,pk)
"""
#generick
"""
class HariList(generics.ListCreateAPIView):
    queryset = HariOne.objects.all()
    serializer_class = HariSerializers


class Hariempdetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = HariOne.objects.all()
    serializer_class = HariSerializers
    # lookup_field = 'id' optional code keen Yt channel
"""

#custom pagination class

class Haripage(PageNumberPagination):
    page_size = 3

# Viewsets

class HariListV(viewsets.ModelViewSet):
    queryset = HariOne.objects.all()
    serializer_class = HariSerializers
    # pagination_class = PageNumberPagination # this will use the deafult pagination in settings.py
    # pagination_class = Haripage # custom pagination 
    pagination_class = LimitOffsetPagination #offset pagination uses limit and offset limit = n.of jason and offest is lika  apg no. cooneccted with settings.py run server to view changes
    # pip intall django-filter    
    # filter_backends =[DjangoFilterBackend] 
    # filterset_fields = ['name','salary']
    # filter_backends =[filters.SearchFilter] #caseissentitive
    # search_fields = ['id','name']
    # search_fields = ['=id','^name'] #search filter [ss] = is same record if data is test you sould enter test not t

    # ordering fileds
    filter_backends =[filters.OrderingFilter]
    ordering_fields = ['name'] #to get all fields order do not add this line
    # to add one more filed for ordering add this in url
    # ?ordering=name&search=1000000.000,id this , and then field in here i have name decending and id is by deafult set to ascending
    ordering =['id'] # deafult ordering filed if user havn't speficy any field


