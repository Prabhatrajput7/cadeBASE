from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from .serializers import RegistrationSerializer


@api_view(['POST'])
def registration_view(request):
    if request.method =="POST":
        ser = RegistrationSerializer(data = request.data)
        d ={}
        if ser.is_valid():
            account = ser.save()
            d['username'] = account.username
            d['email'] = account.email
            return Response(d,status=status.HTTP_201_CREATED)
    return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
