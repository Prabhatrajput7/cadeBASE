from threading import Thread
import queue
# stockpicker = ['APOLLOHOSP.NS', 'BAJAJ-AUTO.NS', 'BAJAJFINSV.NS', 'BAJFINANCE.NS', 'BHARTIARTL.NS', 'BRITANNIA.NS',
#                'CIPLA.NS', 'COALINDIA.NS', 'HDFCLIFE.NS', 'HEROMOTOCO.NS', 'HINDALCO.NS', 'ICICIBANK.NS',
#                'INDUSINDBK.NS', 'ITC.NS', 'KOTAKBANK.NS', 'LT.NS', 'MARUTI.NS', 'MM.NS', 'NESTLEIND.NS',
#                'NTPC.NS', 'ONGC.NS', 'RELIANCE.NS', 'SHREECEM.NS', 'TATACONSUM.NS', 'TATASTEEL.NS', 'TCS.NS',
#                'TECHM.NS', 'TITAN.NS', 'ULTRACEMCO.NS', 'WIPRO.NS']

# stockpicker = ['APOLLOHOSP.NS', 'BAJAJ-AUTO.NS']
# from yahoo_fin.stock_info import *
# thread_list = []
# que = queue.Queue()
#
# data ={}
# for i in range(len(stockpicker)):
#     thread = Thread(target=lambda q, arg1: q.put({stockpicker[i]: get_quote_table(arg1)}), args=(que, stockpicker[i]))
#     thread_list.append(thread)
#     thread_list[i].start()
#
# for thread in thread_list:
#     thread.join()
#
# while not que.empty():
#     result = que.get()
#     data.update(result)
#
# print(data)



"""
working
Thread(target=lambda q, arg1: q.put({stockpicker[i]: get_quote_table(arg1)}), args=(que, stockpicker[i]))

lamda is a fx q and arg1 are the arguments || args=(que, stockpicker[i]) passing this in lambda
q = que, arg1 = stockpicker[i]
q.put({stockpicker[i]: get_quote_table(arg1)})
performing operation and storing in a dict

"""



