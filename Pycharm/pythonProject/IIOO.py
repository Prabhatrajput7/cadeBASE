#myf = open('tesx.txt')
# print(myf.read())
# myf.seek(0)#move the curser at beg
# print(myf.read())
# print(myf.readline()) #line1
# print(myf.readline()) #line2
# print(myf.readline()) #line3
#print(myf.readlines()) #lis contains entire lines
#myf.close()

with open('wt.txt', mode='w') as mf:
    text = mf.write('writt')
    print(text)

