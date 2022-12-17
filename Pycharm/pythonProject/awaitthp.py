# SYNC NAD ASYNC

import time
import asyncio


# def sone():
#     for i in range(3):
#         print(i)
#         time.sleep(1)

# def stwo():
#     for i in range(3,0,-1):
#         print(i)
#         time.sleep(1)

# sone()
# stwo()

async def asone():
    print('one')
    # await astwo()
    asyncio.create_task(astwo())
    print('two')

async def astwo():
    print('fx2')
    await asyncio.sleep(10)

asyncio.run(asone())


import threading

# fx--onesec--fx2--onesec--done

# def none():
#     print('None')
#     time.sleep(1)
#     print('nsleep')

# def ntwo():
#     print('Ntwo')
#     time.sleep(1)
#     print('nsleep')

# none()
# ntwo()

# fx--one--sec--
#   fx2--onesec--done
# time1 =time.perf_counter()

# def tone(a):
#     print(a)
#     time.sleep(1)
#     print('t1sleep')
#
# def ttwo(b):
#     print(b)
#     time.sleep(1)
#     print('t2sleep')
#
# t1 = threading.Thread(target=tone,args=[4])
# t2 = threading.Thread(target=ttwo,args=(4,))
#
# t1.start()
# t2.start()
#
# t1.join()
# t2.join()


# start = time.perf_counter()
#
# def do_something(seconds):
#     print(f'Sleeping {seconds} second(s)...')
#     time.sleep(seconds)
#     return f'Done Sleeping...{seconds}'
#
# threads = []
#
# for _ in range(10):
#     t = threading.Thread(target=do_something, args=[1])
#     t.start()
#     threads.append(t)
#
# for thread in threads:
#     thread.join()
#
# finish = time.perf_counter()
#
# print(f'Finished in {round(finish-start, 2)} second(s)')


# time2 =time.perf_counter()

#  if we dont put join as it start and goes to sleep it execute below code
# print(time2-time1)


# import queue
#
# q = queue.Queue()
# q.push(5)



# class TH(threading.Thread):

#     def __init__(self,totol):
#         self.t = totol
#         threading.Thread.__init__(self)

#     def run(self):
#         for i in range(self.t):
#             print(i)


# t = TH(10)
# t.run()


import multiprocessing
#  multiprocessing
# fx--onesec--
# fx2--onesec--

# time1 =time.perf_counter()

# def pone():
#     print('Pone')
#     time.sleep(1)
#     print('psleep')



# def ptwo():
#     print('ptwo')
#     time.sleep(1)
#     print('psleep')

# p1 = multiprocessing.Process(target=pone)
# p2 = multiprocessing.Process(target=ptwo)


# if __name__ == '__main__':
#     p1.start()
#     p2.start()

#     p1.join()
#     p2.join()

#     time2 =time.perf_counter()
#     print(time2-time1)
