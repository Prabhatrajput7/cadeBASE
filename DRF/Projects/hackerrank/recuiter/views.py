from django.shortcuts import render
from rest_framework import viewsets, response, status, permissions, generics, views
from .serializers import Jdser, ApplicationSer
from userd.models import JD, Application
from rest_framework.authentication import TokenAuthentication
from .permissions import IsOwnProfileOrReadOnly,SeekervsRec
from rest_framework.exceptions import ValidationError
from rest_framework.decorators import action
# Create your views here.


class AllJD(generics.ListCreateAPIView):

    # authentication_classes = (TokenAuthentication,)
    # permission_classes = [permissions.IsAuthenticated,SeekervsRec]
    queryset = JD.objects.all()
    serializer_class = Jdser

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(rec=user)


class Jdetail(generics.RetrieveUpdateDestroyAPIView, generics.GenericAPIView):

    # authentication_classes = (TokenAuthentication,)
    # permission_classes = [permissions.IsAuthenticated,IsOwnProfileOrReadOnly]
    serializer_class = Jdser
    
    def get(self, request, *args, **kwargs): 
        jd =  JD.objects.get(pk = self.kwargs['pk'])
        ser = self.serializer_class(jd)
        return response.Response(ser.data)

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(rec=user)

class JAdetail(views.APIView):

    authentication_classes = (TokenAuthentication,)
    # permission_classes = [permissions.IsAuthenticated,IsOwnProfileOrReadOnly]

    def get(self, request, pk):
        jd =  JD.objects.get(id = pk)
        ser = Jdser(jd)
        return response.Response(ser.data)

    def check(self,jd):
        return Application.objects.filter(seek= self.request.user, job=jd)

    def post(self, request,pk):
        jd = JD.objects.get(id = pk)
        if jd.opening == 0:
            return response.Response({'msg':'No vancy left'})
        if self.check(jd).exists():
            raise ValidationError('You have already Applied :)')
        Application.objects.create(seek= self.request.user, job=jd)
        jd.opening -=1
        jd.save()
        return response.Response({'msg':'Applied successfully'})




class Modelallj(viewsets.ModelViewSet):

    queryset = JD.objects.all()
    serializer_class = Jdser
    # http://127.0.0.1:8000/recuiter/model/all/2/check/
    @action(detail=True, methods=['GET'])
    def check(self, request, pk=None):
        curr = self.get_object()
        ap = Application.objects.filter(job=curr)
        ser = ApplicationSer(ap, many =True)
        return response.Response(ser.data)
