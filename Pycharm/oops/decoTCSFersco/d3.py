import sys
import os


# Define and implement bold_tag

def bold_tag(func):
    def inner(*args, **kwdargs):
        return f'<b>{str(func(*args, **kwdargs))}</b>'

    return inner


@bold_tag
def say(msg):
    return msg


'''Check the Tail section for input/output'''
if __name__ == "__main__":
    with open(os.environ['OUTPUT_PATH'], 'w') as fout:
        res_lst = list()
        res_lst.append(say(input()))
        fout.write("{}".format(*res_lst))