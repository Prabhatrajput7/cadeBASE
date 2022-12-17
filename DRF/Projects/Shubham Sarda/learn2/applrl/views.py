from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from .serializers import RegistrationSerializer
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

@api_view(['POST',])
def logout_view(request):

    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)

@api_view(['POST'])
def registration_view(request):
    if request.method =="POST":
        ser = RegistrationSerializer(data = request.data)
        d ={}
        if ser.is_valid():
            # ser.save()
            # user = User.objects.get(username = ser.data['username'])
            # tok,_ = Token.objects.get_or_create(user=user)
            account = ser.save()
            d['username'] = account.username
            d['email'] = account.email
            """token"""
            token = Token.objects.get(user=account).key
            d['token'] = token
            return Response(d,status=status.HTTP_201_CREATED)
            # return Response({'Payload':ser.data, 'Token':str(tok),'status':status.HTTP_201_CREATED})

            """jwt"""
            # user = User.objects.get(username = account.username)
            # refresh = RefreshToken.for_user(user)
            # refresh = RefreshToken.for_user(account)  --> OR
            # return Response({'payload':ser.data, 'status':status.HTTP_201_CREATED, 'refresh': str(refresh),'access': str(refresh.access_token),})
            # data['token'] = {
            #                     'refresh': str(refresh),
            #                     'access': str(refresh.access_token),
            #                 }
    return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
