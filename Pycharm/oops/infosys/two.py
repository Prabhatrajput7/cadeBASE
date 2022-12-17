def prefXor(n,B):
    bc = B.copy()
    new =[]
    m1 = max(B)
    if B.count(m1)>=2:
        new.append(m1)
    for i in bc:
        try:
            bc.remove(m1)
        except:
            break
    m2 = max(bc)
    if bc.count(m2)>=2:
        new.append(m2)
    return new

n = int(input('>'))
B = []
for _ in range(n):
    B.append(int(input('>')))
print(prefXor(n,B))