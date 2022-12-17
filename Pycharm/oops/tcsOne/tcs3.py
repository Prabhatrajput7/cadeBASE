import ast

# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
Write the function list_oper that takes two list as input.

Function should return a string after performing the operations specified below
 - Check for the squares and cubes of elements in list1 is present in list2
 - Return "Squares and Cubes are present" if squares and cubes of all elements in list1 are present in list2.
 - Return "Squares are only present" if squares of all elements in list1 are only present in list2.
 - Return "Cubes are only present" if cubes of all the elements in list1 are only present in list2.
 - Return "No such pattern is present" if there are squares and cubes of any element in list1 is not present in list2
 [4, 10, 12, 8, 3] [16, 100, 144, 64, 9, 10, 120, 44, 12]
'''


def list_oper(list1, list2):
    sq = [i * i for i in list1]
    cube = [i ** 3 for i in list1]
    if all(item in list2 for item in sq) and all(item in list2 for item in cube):
        return f'Squares and Cubes are present'
    elif all(item in list2 for item in sq):
        return f'Squares are only present'
    elif all(item in list2 for item in cube):
        return f'Cubes are only present'
    else:
        return f'No such pattern is present'


'''
Write the function amstrong which takes two numbers(num1,num2) as input. Function should return the list of amstrong numbers between num1 and num2

Example : [0,1,..]
'''


def amstrong(num1, num2):
    lst = []
    for i in range(num1, num2):
        if sum(int(i) ** 3 for i in str(i)) == i and i > 100:
            lst.append(i)
    return lst


'''
Write the function string_oper which takes a string as input and return another string after removing words that have characters repeated

Input : "This is an example"
Output : "This is an"
'''

def string_oper(string1):
    s1 = string1.split()
    s2 = list(filter(lambda x:all(x.count(i)<2 for i in x),s1))
    return ' '.join(s2)


'''
Write a function string_reverse which takes a string as input and return another string with each word in reversed order.

Example : "START OF THE PROJECT"
Output :  "TRATS FO EHT TCEJORP"
'''


def string_reverse(string2):
    s1 = string2.split(' ')
    s1 = [i[::-1] for i in s1]
    return ' '.join(s1)


if __name__ == '__main__':
    list1 = ast.literal_eval(input())
    list2 = ast.literal_eval(input())
    num1 = ast.literal_eval(input())
    num2 = ast.literal_eval(input())
    string1 = input()
    string2 = input()
    print(list_oper(list1, list2))
    print(amstrong(num1, num2))
    print(string_oper(string1))
    print(string_reverse(string2))
