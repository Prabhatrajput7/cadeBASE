from random import randint

answer = randint(0, 11)
while True:
    try:
        guess = int(input('Enter a no. b/w 0-10: '))
        if 0 < guess < 11:
            if answer == guess:
                print(f'{guess} -> Yeah that\'s the one')
                break
        elif guess < 0:
            print('Daam it A +ve number plzz')

    except ValueError:
        print('Hey bozo, I said number')
