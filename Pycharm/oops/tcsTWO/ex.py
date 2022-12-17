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


    # for i in contents:
    #     for j in i:
    #         if len(i) < 2:
    #             print('Number of Inputs should be more than one')
    #         if '0' in j:
    #             print('Second value should not be zero')

if __name__ == '__main__':
    contents = []
    while True:
        a = input().split()
        if a:
            contents.append(a)
        else:
            break
    handelExe(contents)

# n = 5
# try:
#     n*2
# except:
#     print('err')
# else:
#     print('2')