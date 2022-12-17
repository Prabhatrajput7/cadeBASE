import imp
from django.shortcuts import render
from rest_framework import exceptions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer, LUserSerializer, AUserSerializer
from app.models import User
from rest_framework import generics
from .authjwt import JWTauth
# Create your views here.

class RegisterAPIView(APIView):

    # serializer_class = UserSerializer

    def post(self, request):

        data = request.data
        if data['password'] != data['password_confirm']:
            raise exceptions.APIException('Passwords do not match!')

        data['is_ambassador'] = 1 if 'api/ambassador' in request.path else  0

        serializer = AUserSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

        # serializer = self.serializer_class(data=request.data)
        # if serializer.is_valid(raise_exception=True):
        #     serializer.save()
        #     return Response(serializer.data)
        # else:
        #     return Response(serializer.errors)


class LoginAPIView(APIView):

    # serializer_class = LUserSerializer

    def post(self, request):

        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()

        if user is None:
            raise exceptions.AuthenticationFailed('User not found!')

        if not user.check_password(password):
            raise exceptions.AuthenticationFailed('Incorrect Password!')

        scope = 'ambassador' if 'api/ambassador' in request.path else 'admin'

        # scope = 'ambassador' if user.is_ambassador else 'admin'

        if user.is_ambassador and scope == 'admin':
            raise exceptions.AuthenticationFailed('Unauthorized')

        token = JWTauth.generate_jwt(user.id, scope)

        response = Response()
        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
        'message': 'success'
        }

        return response

        # serializer = self.serializer_class(data=request.data)
        # if serializer.is_valid(raise_exception=True):
        #     email = serializer.data.get('email')
        #     password = serializer.data.get('password')

        #     user = User.objects.filter(email=email).first()

        #     if user is None:
        #         raise exceptions.AuthenticationFailed('User not found!')

        #     if not user.check_password(password):
        #         raise exceptions.AuthenticationFailed('Incorrect Password!')

        #     token = JWTauth.generate_jwt(user.id)

        #     response = Response()
        #     response.set_cookie(key='jwt', value=token, httponly=True)
        #     response.data = {
        #     'message': 'success'
        #     }

        #     return response

            # return Response({
            #     'msg':'login successfull',
            #     'jwt':token
            #     })

        # else:
        #     return Response(serializer.errors)


class UserAPI(APIView):

    authentication_classes = [JWTauth]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        data = AUserSerializer(user).data
        if 'api/ambassador' in request.path:
            data['revenue'] = user.revenue
        data['name'] = user.name
        return Response(data)
        # return Response(AUserSerializer(request.user).data)


class LogoutAPIView(APIView):
    authentication_classes = [JWTauth]
    permission_classes = [IsAuthenticated]

    def post(self, _):
        response = Response()
        response.delete_cookie(key='jwt')
        response.data = {
            'message': 'success'
        }
        return response

class ProfileInfoAPIView(APIView):
    authentication_classes = [JWTauth]
    permission_classes = [IsAuthenticated]

    def put(self, request, pk=None):
        user = request.user
        serializer = AUserSerializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)        

class ProfilePasswordAPIView(APIView):
    authentication_classes = [JWTauth]
    permission_classes = [IsAuthenticated]

    def put(self, request, pk=None):
        user = request.user
        data = request.data

        if data['password'] != data['password_confirm']:
            raise exceptions.APIException('Passwords do not match!')

        user.set_password(data['password'])
        user.save()
        return Response(AUserSerializer(user).data)        