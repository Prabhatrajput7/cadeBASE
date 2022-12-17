import collections


# Enter your code here. Read input from STDIN. Print output to STDOUT


def printDic(d):
    for i, j in d.items():
        print(f'{j} is the value of the key {i}')


def actionDic(old_dic):
    strInput = list(map(str, input().split()))
    print(strInput)
    numInput = list(map(int, input().split()))
    d = {j: numInput[i] for i, j in enumerate(strInput)}
    d.update(old_dic)
    printDic(d)


def getEven(n):
    print(sum(i for i in range(n + 1) if i % 2 == 0))


if __name__ == '__main__':
    old_dic = {'ram': 6, 'mouse': 4, 'monitor': 3}
    actionDic(old_dic)
    n = int(input())
    getEven(n)