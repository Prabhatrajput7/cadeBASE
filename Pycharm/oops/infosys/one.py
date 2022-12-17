def prefXor(n,B):
    new =[B[0]]
    try:
        for i in range(len(B)):
            x = B[i] ^ B[i+1]
            new.append(x)
    except IndexError:
        return new
n = int(input('>'))
B = []
for _ in range(n):
    B.append(int(input('>')))
print(prefXor(n,B))