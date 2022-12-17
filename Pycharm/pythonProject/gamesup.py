from random import randint
import sys

def games(guess, answer):
    if 0 < int(guess) < 11:
        if answer == int(guess):
            return True
    else:
        print('1-5 PLZ')

if __name__ == '__main__':
    answer = randint(1,5)
    while True:
        try:
            guess = input('enter a no. b/w 1-5: ')
            if games(guess,answer):
                break
        except ValueError:
            print('plz enter a no. b/w 1-5')
