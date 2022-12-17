from django.shortcuts import render
from store.models import Product

def check(request):
    context = {
        'product':Product.objects.filter(is_available =True).order_by('-id')
    }
    return render(request,'home.html',context)