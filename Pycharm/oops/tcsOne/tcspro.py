import ast

# Enter your code here. Read input from STDIN. Print output to STDOUT
import ast


def numbers(num1, num2, num3, num4):
    '''
    Find the sum of all the numbers and store it in variable sum_of_numbers
    '''
    lst  = [num1, num2, num3, num4]
    sum_of_numbers = sum(lst)

    '''
    Find the sum of float numbers among the numbers and store it in variable sum_of_float_numbers
    '''

    sum_of_float_numbers = sum(i for i in lst if type(i)==float)

    '''
    Find the smallest integer number among the numbers and store it in variable min_number
    '''

    min_number = min(i for i in lst if type(i)==int)

    '''
    Find the count of prime numbers among the numbers and store it in variable prime_count
    '''
    l = []
    def prime(n):
        if type(n) == int:
            return all(n%i for i in range(2,int(n/2)+1)) and n >1
    for i in lst:
        if prime(i):
            l.append(i)

    prime_count = len(l)

    '''
    Check for zeros. If there are zeros present among the numbers, store True else store False in the variable zero_check
    '''

    zero_check = bool(0 in lst)

    print(sum_of_numbers)
    print(sum_of_float_numbers)
    print(min_number)
    print(prime_count)
    print(zero_check)


if __name__ == '__main__':
    num1 = ast.literal_eval(input())
    num2 = ast.literal_eval(input())
    num3 = ast.literal_eval(input())
    num4 = ast.literal_eval(input())
    numbers(num1, num2, num3, num4)