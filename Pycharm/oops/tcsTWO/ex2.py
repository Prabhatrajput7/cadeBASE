# Enter your code here. Read input from STDIN. Print output to STDOUT

def handelExe(contents):

    for i in contents:
        try:
            Z = [int(j) for j in i]
        except:
            print('Enter a valid numbers')
            continue
        try:
            assert len(i)>1
        except:
            print('Number of Inputs should be more than one')
            continue
        try:
            if '0' in i:
                assert '0' != i[1]
        except:
            print('Second value should not be zero')
            continue
        try:
            assert sum(int(j) for j in i)<= 100
        except:
            print('Sum of the list should be less than 100')
            print(sum(int(j) for j in i))
            continue
        try:
            print(int(i[0])/int(i[1]))
            print('File not found\nCode has been executed')
        except:
            pass

if __name__ == '__main__':
    contents = []
    while True:
        try:
            line = input().split()
        except EOFError:
            break
        contents.append(line)
    handelExe(contents)

a,b = 5,5

assert a!=b