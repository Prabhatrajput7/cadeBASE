from django.shortcuts import render
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.core.cache import cache
from .models import Attack
from django.http import HttpRequest,HttpResponse,HttpResponseRedirect

CACHE_TTL = getattr(settings ,'CACHE_TTL' , DEFAULT_TIMEOUT)
# Create your views here.

def allattack(request):
    att = Attack.objects.all()
    return render(request,'app/all.html',{'all':att})


def individual(request,pk):
    if cache.get(pk):
        print("DATA COMING FROM CACHE")
        att = cache.get(pk)
    else:
        print("DATA COMING FROM DB")
        att = Attack.objects.get(id = pk)
        cache.set(pk , att)
    return render(request,'app/individual.html',{'att':att})

