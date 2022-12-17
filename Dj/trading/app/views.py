from django.shortcuts import render
from yahoo_fin.stock_info import *
import time
import queue
from threading import Thread
import json
# Create your views here.

def stockerp(request):
    stockpicker = tickers_nifty50()
    return render(request,'app/stockpic.html',{'stockpicker':stockpicker})

def stockert(request):
    stockpicker = request.GET.getlist('stockpicker')
    data ={}

    thread_list = []
    que = queue.Queue()

    for i in range(len(stockpicker)):
        thread = Thread(target = lambda q, arg1: q.put({stockpicker[i]: get_quote_table(arg1)}), args = (que, stockpicker[i]))
        thread_list.append(thread)
        thread_list[i].start()

    for thread in thread_list:
        thread.join()

    while not que.empty():
        result = que.get()
        data.update(result)

    return render(request,'app/stocktra.html',{'data':data})    

    """
    stockpicker = request.GET.getlist('stockpicker')
    old code
    data = {}
    for i in stockpicker:
        if i in available_stocks:
            pass
        else:
            return HttpResponse("Error")
    # for i in stockpicker:
    #     result = get_quote_table(i)
    #     data.update({i: result})
    """















# code knee
# from django.views.decorators.csrf import csrf_exempt
# @csrf_exempt
    
    # print(request.body)
    # try:
    #     data = json.loads(request.body)
    #     if data:
    #         print(data)
    # except Exception as E:
    #     print(E)