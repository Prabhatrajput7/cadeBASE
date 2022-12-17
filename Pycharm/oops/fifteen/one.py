def last(lst):
    for i in lst:
        s = sum(int(j) for j in i)
        if len(str(s))>=2:
            yield sum(int(j) for j in str(s))
        else:
            yield s
num = int(input('>'))
lst =[]
for i in range(0,num):
    lst.append(input('>'))
for i,j in enumerate(last(lst)):
    print(lst[i]+str(j))