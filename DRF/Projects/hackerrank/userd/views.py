from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status, generics, viewsets, permissions
from rest_framework.views import APIView
from yaml import serialize
from .models import User
from .serilizers import LoginSer, ProfileSer, ProfileUpdate, PasswordChg, RegSer
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.authentication import TokenAuthentication
# Create your views here.

class Register(generics.GenericAPIView):

    serializer_class =  RegSer

    def post(self, request):
        seeker = 1 if 'seeker/register/' in request.path else 0
        rec = 1 if 'recuiter/register/' in request.path else 0
        serializer = self.serializer_class(data=request.data,context={'is_seeker':seeker,'is_rec':rec})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"msg":"Registered Successfully"})


class Login(generics.GenericAPIView):
    
    serializer_class = LoginSer

    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.data.get('username')
        password = serializer.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            tok,_ = Token.objects.get_or_create(user=user)
            return Response({'Token':str(tok),'msg':'Login Success'}, status=status.HTTP_200_OK)
        else:
            return Response({'errors':'Username or Password is not Valid'}, status=status.HTTP_404_NOT_FOUND)


class Logout(APIView):

    authentication_classes = (TokenAuthentication,)
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        self.request.user.auth_token.delete()
        return Response({'msg':'Logout Successful'},status=status.HTTP_200_OK)

class Profile(APIView):

    authentication_classes = (TokenAuthentication,)
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):

        ser = ProfileSer(self.request.user)
        return Response(ser.data)

class ProfileUP(generics.GenericAPIView):

    serializer_class =ProfileUpdate
    authentication_classes = (TokenAuthentication,)
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, pk=None):
        user = self.request.user
        serializer = self.serializer_class(user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def patch(self, request, pk=None):
        user = self.request.user
        serializer = self.serializer_class(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class PasswordProfile(generics.GenericAPIView):

    serializer_class = PasswordChg
    authentication_classes = (TokenAuthentication,)
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        p1 = serializer.data.get('password')
        p2 = serializer.data.get('password2')
        if p1 != p2:
            return Response({"Error":"Password and Confirm Password doesn't match"})
        user = self.request.user
        user.set_password(p1)
        user.save()
        return Response({'msg':'Password Changed Successfully'}, status=status.HTTP_200_OK)

            
        