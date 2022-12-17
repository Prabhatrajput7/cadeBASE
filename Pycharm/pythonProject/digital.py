def line(r,stu):
    stu.sort()
    if r in stu:
        idx = stu.index(r)
        return idx
    else:
        for i in stu:
            if i > r:
                edx = stu.index(i)
                break
        return edx
if __name__ == '__main__':
    n = abs(int(input('>')))
    r = abs(int(input('>')))
    stu = []
    for i in range(n):
        stu.append(abs(int(input('>'))))
    print(line(r,stu))
