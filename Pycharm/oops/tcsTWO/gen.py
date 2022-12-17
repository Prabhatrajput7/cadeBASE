# Enter your code here. Read input from STDIN. Print output to STDOUT

def generator_sum(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        temp = a
        a = b
        b = temp + b


if __name__ == '__main__':
    n = int(input())
    l = []
    for i in generator_sum(n):
        l.append(i)
    print(sum([i * i for i in l]))