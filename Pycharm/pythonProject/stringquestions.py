a = 'aabbccdda'
d = {}.fromkeys(a,0)
for i in a:
    d[i] +=1
st = ''
for s in d:
    st += s+str(d[s])
    st+= ' '
print(st)






