import os
import sys


def italic_tag(func):
    def inner(*args, **kwdargs):
        return '<i>' + func(*args, **kwdargs) + '</i>'

    return inner


# Implement italic_tag below

@italic_tag
def say(msg):
    return msg


'''Check the Tail section for input/output'''
if __name__ == "__main__":
    with open(os.environ['OUTPUT_PATH'], 'w') as fout:
        res_lst = list()
        res_lst.append(say(input()))
        fout.write("{}".format(*res_lst))