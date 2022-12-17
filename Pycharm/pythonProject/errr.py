# while True:
#     try:
#         no = int(input('>'))/0
#     except ZeroDivisionError:
#         print('Cant divide with zero')
#         break
#     else:
#         print('else')
#         break

l =[0,1,2]
while True:
    try:
        num = input('enter a number b/w 0-2 -> ')
        value = input('enter a value -> ')
    except ValueError as err:
        print(err)
    else:
        try:
            l[int(num)] = value
            print(l)
            print('q for quit and c for continue')
            v = input('>')
            if v =='q':
                print('Your final list ', l)
                break
            else:
                continue
        except IndexError as err:
            print(err)
