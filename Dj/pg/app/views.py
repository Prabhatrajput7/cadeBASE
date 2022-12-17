from multiprocessing import context
from django.shortcuts import redirect, render
from .models import Product, R6
from django.contrib.auth.decorators import login_required
from django.db import connection
from django.db.models import Q
from .grp import mine_group_required,CheckPremiumGroupMixin
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


@login_required(login_url='login')
def subdomaincheck(request):
    context = {
        'p': Product.objects.all()
    }
    return render(request,'app/sub.html',context)

@login_required(login_url='login')
# @mine_group_required(allowed_grp=['Premium'])
@mine_group_required('Premium')
def siege(request):

    o = R6.objects.all()
    l0 = list(o)
    l0.append('query')
    f = R6.objects.filter(is_del = False)

    context ={
        'obj': o,
        'l': l0,
        'value':R6.objects.values(),
        'lst':R6.objects.values_list('op',flat=True),
        'tuple':R6.objects.values_list(),
        'fobj':f
    }

    return render(request,'app/siege.html',context)   

def siegeid(request,id):
    pk = R6.objects.get(id=id)
    pk.is_del = True
    pk.save()
    return redirect('siege')
# Raw Query

def raw(request):

    raw = R6.objects.raw('SELECT * FROM app_r6')
    context={
        'raw':raw
    }
    return render(request,'app/raw.html',context)

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    #cursor.description (('id', None, None, None, None, None, None), ('op', None, None, None, None, None, None), ('speed', None, None, None, None, None, None), ('side', None, None, None, None, None, None))
    #colums['id', 'op', 'speed', 'side']
    # c = ['id', 'op', 'speed', 'side']
    #d = (1, 'Ash', 3, 'Attack')
    # print(dict(zip(c,d)))
    # for row in cursor.fetchall():
    #     print(row)
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]    

def rawsql(request):
    c = connection.cursor()
    c.execute('SELECT * FROM app_r6')
    cd = dictfetchall(c)
    context ={
        'c':cd
    }
    return render(request, 'app/rawsql.html',context)    

class Siege(LoginRequiredMixin,ListView):
    login_url = '/login/'
    redirect_field_name = 'login'
    model = R6
    template_name = 'app/list_class_check.html'