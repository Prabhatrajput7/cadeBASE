from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from app.models import Movie
from app.serializers import MovieSerial
# Create your views here.
"""
@api_view(['GET','POST'])
def MovieNS(request):
    if request.method == 'GET':
        mov = Movie.objects.all()
        ser = MovieSerial(mov, many=True)
        return Response(ser.data, status = status.HTTP_201_CREATED)

    elif request.method == 'POST':
        ser = MovieSerial(data= request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status = status.HTTP_201_CREATED)
        return Response(ser.data, status = status.HTTP_400_BAD_REQUEST)
"""
"""
@api_view(['GET','PUT','DELETE','PATCH'])
def MoviePK(request,pk):
    try:
        one = Movie.objects.get(id=pk)
    except:
        return Response({'NF':'Not Found'},status = status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        ser = MovieSerial(one)
        return Response({'data':ser.data}, status = status.HTTP_201_CREATED)

#         {
#     "data": {
#         "id": 1,
#         "name": "spiderman 1",
#         "description": "Tobey Goblin",
#         "active": false
#     }
# }


    elif request.method == 'PUT':
        ser = MovieSerial(one, data= request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status = status.HTTP_201_CREATED)
        return Response(ser.data, status = status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PATCH':
        ser = MovieSerial(one, data= request.data, partial=True)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status = status.HTTP_201_CREATED)
        return Response(ser.data, status = status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        one.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
"""


###############################################################
from rest_framework.views import APIView
from django.http import Http404

class Movieclass(APIView):
    
    def get(self,request):
        mov = Movie.objects.all()
        ser = MovieSerial(mov, many=True,context={'request': request})
        return Response(ser.data, status = status.HTTP_201_CREATED)

    def post(self,request):
        ser = MovieSerial(data= request.data,context={'request': request})
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status = status.HTTP_201_CREATED)
        # return Response(ser.data, status = status.HTTP_400_BAD_REQUEST)
        return Response(ser.errors)
        """to print the erros user errors"""


class MovieclassPK(APIView):
    
    def getting(self,pk):
        try:
            one = Movie.objects.get(id=pk)
            return one
        except:
            raise Http404

    def get(self,request,pk):
        one = self.getting(pk)
        ser = MovieSerial(one,context={'request': request})
        return Response(ser.data, status = status.HTTP_201_CREATED)

    def put(self,request,pk):
        one = self.getting(pk)
        ser = MovieSerial(one, data= request.data,context={'request': request})
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status = status.HTTP_201_CREATED)
        return Response(ser.data, status = status.HTTP_400_BAD_REQUEST)

    def patch(self,request,pk):
        one = self.getting(pk)
        ser = MovieSerial(one, data= request.data, partial=True,context={'request': request})
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status = status.HTTP_201_CREATED)
        return Response(ser.data, status = status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        one = self.getting(pk)
        one.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)        