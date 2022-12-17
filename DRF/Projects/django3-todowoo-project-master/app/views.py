from django.shortcuts import render
from itsdangerous import Serializer
from rest_framework import generics, permissions
from todo.models import Todo
from app.serializers import TodoCompleteSerializer,TodoSerializer
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from django.db import IntegrityError
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from app.permission import IsOwnProfileOrReadOnly
# Create your views here.        

class TodoComplete(generics.UpdateAPIView):
    # queryset = Todo.objects.select_related('user').all()
    serializer_class = TodoCompleteSerializer
    permission_classes = [permissions.IsAuthenticated,IsOwnProfileOrReadOnly]

    def get_queryset(self):
        # print(Todo.objects.filter(user = self.request.user, pk = self.kwargs['pk']))
        return Todo.objects.filter(user = self.request.user, pk = self.kwargs['pk'])

    def perform_update(self, serializer):
        serializer.instance.datecompleted = timezone.now()
        # serializer.instance.memo = 'I am updated for no reason'
        serializer.save()
        
class TodoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.select_related('user').all()
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated,IsOwnProfileOrReadOnly]
    # def get_queryset(self):
    #     return Todo.objects.filter(user = self.request.user.id)

class TodoListCreate(generics.ListCreateAPIView):
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user__username=user.username, datecompleted__isnull=True)

    def perform_create(self, serializer):
        # print(serializer.data)
        user = self.request.user
        serializer.save(user=user)


class TodoCompletedList(generics.ListAPIView):
    serializer_class = TodoCompleteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user__username=user, datecompleted__isnull=False).order_by('-datecompleted')

"""
@csrf_exempt
def signup(request):
    if request.method == 'POST':
        try:
            data = JSONParser().parse(request)
            user = User.objects.create_user(username=data['username'], password=data['password'])
            user.save()
            token = Token.objects.create(user=user)
            return JsonResponse({'token':str(token)}, status=201)
        except IntegrityError:
            return JsonResponse({'error':'That username has already been taken. Please choose a new username'}, status=400)

@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        user = authenticate(request, username=data['username'], password=data['password'])
        if user is None:
            return JsonResponse({'error':'Could not login. Please check username and password'}, status=400)
        else:
            try:
                token = Token.objects.get(user=user)
            except:
                token = Token.objects.create(user=user)
            return JsonResponse({'token':str(token)}, status=200)    
"""        