from django.shortcuts import render, redirect
from .models import *
from django.http import Http404, HttpResponseRedirect
from .forms import *
from django.urls import reverse
from django.forms import formset_factory
from django.forms import inlineformset_factory
from .filters import OrderFilter
# Create your views here.

def home(request):
    o = Order.objects
    c = Customer.objects.all()

    context = {
        'order': o.all(),
        'customer': c,
        'to':o.all().count(),
        'od':o.filter(status='Delivered').count(),
        'op':o.filter(status='Pending').count()
    }
    return render(request,'app/dashboard.html',context)

def product(request):
    p = Product.objects.all()
    return render(request,'app/product.html',{'product':p})

# filter
def customer(request, pk=None):
    try:
        c = Customer.objects.get(id=pk)
        cpro = c.order_set.all()
    except:
        raise Http404
    
    mfilter = OrderFilter(request.GET, queryset=cpro)
    cpro =mfilter.qs

    context = {
        'c':c,
        'cpro':cpro,
        'ctotal':cpro.count(),
        'mfilter':mfilter
    }
    return render(request,'app/customer.html', context)        


def createorder(request):
    if request.method == "POST":
        orderform = OrderForm(request.POST)
        if orderform.is_valid():
            orderform.save()
            return redirect('home')

    else:
        orderform = OrderForm()
    return render(request,'app/createorder.html',{'form':orderform})


def updateord(request, pk):
    o = Order.objects.get(id=pk)
    if request.method == 'POST':
        orderform = OrderForm(request.POST,instance=o)
        if orderform.is_valid():
            orderform.save()
            return redirect('home')
    else:
        orderform = OrderForm(instance=o)
    return render(request,'app/createorder.html',{'form':orderform})


def deleteord(request, pk):
    o = Order.objects.get(id=pk)
    o.delete()
    return redirect('home')     


def creatcustomer(request):
    if request.method == "POST":
        custform = CustForm(request.POST)
        if custform.is_valid():
            custform.save()
            return redirect('home')

    else:
        custform = CustForm()
    return render(request,'app/createcustomer.html',{'form':CustForm})    

# post or none
def placecust(request,pk=None): 
    c = Customer.objects.get(id=pk)
    GeeksFormSet = formset_factory(OrderFormCust, extra = 2)
    formset = GeeksFormSet(request.POST or None)
    if formset.is_valid():
        for form in formset:
            f = form.save()
            f.customer_id = c
            f.save()
        return HttpResponseRedirect('/product') #make sure to add / if using only returhttpresredirec.
        # print(HttpResponseRedirect(reverse('customerdetail', args=[c.id])))
        # <HttpResponseRedirect status_code=302, "text/html; charset=utf-8", url="/customer/1/">
        return HttpResponseRedirect(reverse('customerdetail', args=[c.id]))
    return render(request,'app/createorder.html',{'form':formset})   

"""
# orderform = OrderForm(initial={'customer':c})
# initial={'customer':c} customer model name
learning 

request.post or none
formset
filter
initial

"""  

def updatecust(request, pk):
    c = Customer.objects.get(id=pk)
    if request.method == 'POST':
        custform = CustForm(request.POST,instance=c)
        if custform.is_valid():
            custform.save()
            return HttpResponseRedirect(reverse('customerdetail', args=[c.id]))
    else:
        custform = CustForm(instance=c)
    return render(request,'app/createcustomer.html',{'form':custform})

def deletecust(request, pk):
    c = Customer.objects.get(id=pk)
    c.delete()
    return redirect('home')       


