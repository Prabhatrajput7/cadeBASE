from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import Filelist, GeeksSerializer
# Create your views here.


class HandleFile(APIView):

    def post(self,request):
        try:
            data = request.data
            ser = Filelist(data=data)
            if ser.is_valid():
                print('one')
                d = ser.save()
                print('two')
                return Response ({
                    'status':200,
                    'msg':'fileuploaded',
                    'data': d
                })
            else:
                return Response({
                    'status':400,
                    'msg':'something went wrong',
                    'data': ser.errors
                })
        except Exception as e:
            print(e)

class GHandleFile(APIView):

    def post(self,request):
        try:
            data = request.data
            ser = GeeksSerializer(data=data)
            if ser.is_valid():
                d = ser.save()
                return Response ({
                    'status':200,
                    'msg':'fileuploaded',
                    'data': d
                })
            else:
                return Response({
                    'status':400,
                    'msg':'something went wrong',
                    'data': ser.errors
                })
        except Exception as e:
            print(e)            