from django.shortcuts import render
from .task import *
from django.http import HttpResponse
# Create your views here.
"""
import celery fx here and put.delay()
like fxname.delay()
"""

def sleppy(request):
    delaay(10)
    delaay.delay(10)
    return HttpResponse('<h1>Celey</h1>')

