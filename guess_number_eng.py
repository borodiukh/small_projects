import random


def is_valid(input_s, right_s):
    if input_s.isdigit() and 1 <= int(input_s) <= right_s:
        return True
    else:
        return False


def is_valid_right_s(input_s):
    if input_s.isdigit() and int(input_s) > 1:
        return True
    else:
        return False


def correct_answer(answer):
    if answer == 'yes' or answer == 'no':
        return False
    return True


def game():
    print('Welcome in game \'Guess number\'')
    right_s = input('I would like guess number from 1 to: (input number and press \'enter\') ')

    while not is_valid_right_s(right_s):
        print('You input not a number or number is less then 1 or number equal 1')
        right_s = input('I would like guess number from 1 to: (input number and press \'enter\') ')

    right_s = int(right_s)
    print(f'Try guess number from 1 to {right_s}')
    num = random.randint(1, right_s)
    total_try = 0

    while True:
        prop = input()
        while not is_valid(prop, right_s):
            print(f'Please input integer number from 1 to {right_s}?')
            prop = input()
        prop = int(prop)
        total_try += 1
        if prop < num:
            print('Too little, try again')
            continue
        elif prop > num:
            print('Too many, try again')
            continue
        elif prop == num:
            print()
            print('You guess, my congratulation!')
            print('Number of attempts: {}'.format(total_try))
            print()
            answer = input("Do you want to play again? Input 'yes' або 'no': ")
            while correct_answer(answer):
                answer = input("Do you want to play again? Input 'yes' або 'no': ")
            print()
            if answer == 'yes':
                break
            elif answer == 'no':
                print('Thanks for playing my game')
                print('Author: Yurii')
                print('All rights reserved')
                global game_on
                game_on = False
                break


game_on = True

while game_on:
    game()

print()
input('Press for exit ')
