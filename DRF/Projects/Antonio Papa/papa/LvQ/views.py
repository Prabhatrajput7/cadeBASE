from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import LQ
from .serializers import SLQ
# Create your views here.


@api_view(['GET'])
def lq(request):

    if request.method == "GET":
        l = list(LQ.objects.all())
        ser = SLQ(l, many= True)
        return Response(ser.data)
            