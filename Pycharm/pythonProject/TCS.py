import math
import os
import random
import re
import sys


# def stringmethod(para, special1, special2, list1, strfind):
#     word1 = para
#     for i in special1:
#         word1 = word1.replace(i, '')
#     word2 = word1[0:70]
#     word2 = word2[::-1]
#     print(word2)
#     l = special2.join(list(word2.replace(" ", '')))
#     print('special',special2)
#     print(l)
#     count = 0
#     for i in list1:
#         if (i in para): count += 1
#     if count == len(list1):
#         print("Every string in ", list1, "were present")
#     else:
#         print("Every string in ", list1, "were not present")
#     print(word1.split()[0:20])
#     list2 = list()
#     freq = []
#     for i in word1.split(" "):
#         if word1.count(i) < 13:
#             if i in freq:
#                 pass
#             else:
#                 freq.append(i)
#     list2 = freq[-1:-21:-1]
#     print(list2[-1:-21:-1])
#     print(word1.rindex(strfind))
#     # Write your code here
#
#
# if __name__ == '__main__':
#     para = input()
#
#     spch1 = input()
#
#     spch2 = input()
#
#     qw1_count = int(input().strip())
#
#     qw1 = []
#
#     for _ in range(qw1_count):
#         qw1_item = input()
#         qw1.append(qw1_item)
#
#     strf = input()
#
#     stringmethod(para, spch1, spch2, qw1, strf)


class MinimumDepositError(Exception):
    def __init__(self):
        raise ValueError("The Minimum amount of Deposit should be 2000.")

class MinimumBalanceError(Exception):
    def __init__(self):
        raise ValueError("You cannot withdraw this amount due to the Minimum Balance Policy")

def Bank_ATM(balance, choice, amount):
    if balance < 500:
        raise ValueError("As per the Minimum Balance Policy, Balance must be at least 500")
    elif choice == 1:
        if amount < 2000:
            MinimumDepositError()
        else:
            balance += amount
            print("Updated Balance Amount: ", balance)
    elif choice == 2:
        p = amount + 500
        if balance < p:
            MinimumBalanceError()
        else:
            balance -= amount
            print("Updated Balance Amount: ", balance)

if __name__ == '__main__':
    bal = int(input())
    ch = int(input())
    amt = int(input())
    try:
        Bank_ATM(bal, ch, amt)
    except ValueError as e:
        print(e)
    except MinimumDepositError as e:
        print(e)
    except MinimumBalanceError as e:
        print(e)

# def myfunc1():
#     x = "John"
#     def myfunc2():
#         nonlocal x
#         x = "hello"
#     myfunc2()
#     return x
# print(myfunc1())