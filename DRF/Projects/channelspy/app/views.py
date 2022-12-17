import imp
from django.shortcuts import render
from .models import Chat, Group
# Create your views here.
def wc(request,grpnm):
    gp = Group.objects.filter(name= grpnm).first()
    if gp:
        chats = Chat.objects.filter(grp=gp)
    else:
        chats =[]
        Group.objects.create(name=grpnm)
    return render(request,'app/chat.html',{'grpnm':grpnm,'chats':chats})
    # return render(request,'app/index.html')

def mywc(request):
    return render(request,'app/three.html')    

def chat2(request,grpnm):
    return render(request,'app/chat2.html',{'grpnm':grpnm})    


# to send message to client outside the consumers
#  this is not a good approcs

from channels.layers import get_channel_layer
from django.http import HttpResponse
from asgiref.sync import async_to_sync

def outside(request):
    ch = get_channel_layer()
    async_to_sync(ch.group_send)('india',{
    'type':'chat.message',
    'message':'message'
    })

    return HttpResponse('Message sent')