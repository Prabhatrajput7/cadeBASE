from django.shortcuts import render
from django.shortcuts import render, HttpResponse
from channels.layers import get_channel_layer
import json

# Create your views here.
def index(request):
    return render(request,'mainapp/index.html',{
        'room_name': "broadcast"
    })


