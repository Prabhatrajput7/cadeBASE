from django.shortcuts import render

# Create your views here.
def s1(request):
    return render(request,'imgg/index.html')