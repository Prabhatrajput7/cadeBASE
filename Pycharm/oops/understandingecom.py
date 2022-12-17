# l = {'links': ['<Category: jacket>', '<Category: jeans>', '<Category: shirts>', '<Category: shoes>', '<Category: tshirts>']}
# for i in l['links']:
#     print(i)

# import datetime
#
# time_th = datetime.datetime.now()-datetime.timedelta(hours=2)
# t = datetime.datetime.now().time()
# t2 =datetime.timedelta(hours=2)
# print(t2)

l = [2,3,17,6,5,1,0]
l2 =[]
for i in range(len(l)-1):
    if l[i]>l[i+1]:
        l2.append(l[i])
l2.append(l[-1])
print(l2)

