from random import randint
import sys

answer = randint(int(sys.argv[1]), int(sys.argv[2]))

while True:
    try:
        guess = int(input(f'guess a number {sys.argv[1]}~{sys.argv[2]}:  '))
        if  0 < guess < 11:
            if guess == answer:
                print('you are a genius!')
                break
        else:
            print(f'hey bozo, I said {sys.argv[1]}~{sys.argv[2]}')
    except ValueError:
        print('please enter a number')
        continue

# i = 1_00_00
# print(f'{i:,}')