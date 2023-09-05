from random import randint


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


def check_user_input(user_input):
    if user_input in ['0', '1', '2']:
        return True
    return False


def yes_or_no(user_input):
    if user_input.lower() in ['yes', 'no']:
        return True
    return False


def determinate_winner(computer_choose, user_choose):
    if computer_choose == 0:
        if user_choose == 0:
            print('DRAW')
        elif user_choose == 1:
            print('YOU WIN. MY CONGRATULATION.')
        elif user_choose == 2:
            print('YOU LOSE')
    if computer_choose == 1:
        if user_choose == 1:
            print('DRAW')
        elif user_choose == 2:
            print('YOU WIN. MY CONGRATULATION.')
        elif user_choose == 0:
            print('YOU LOSE')
    if computer_choose == 2:
        if user_choose == 2:
            print('DRAW')
        elif user_choose == 0:
            print('YOU WIN. MY CONGRATULATION.')
        elif user_choose == 1:
            print('YOU LOSE')


def game():
    signals = [rock, paper, scissors]

    print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
    user_choose = input("Type here: ")
    print()

    while check_user_input(user_choose) == False:
        print('Only digits "0", "1", "2"')
        user_choose = input('Type 0 for Rock, 1 for Paper or 2 for Scissors.\nType here: ')
        print()

    computer_choose = randint(0, 2)
    print(f'Computer choose: {signals[computer_choose]}')
    print(f'You choose: {signals[int(user_choose)]}')

    determinate_winner(computer_choose, int(user_choose))
    print()

    global play_again
    play_again = input('Do you want to play again? Type "yes" or "no" ')
    while yes_or_no(play_again) == False:
        print()
        print('Only "yes" or "no"')
        play_again = input('Do you want to play again? Type "yes" or "no" ')

    if play_again.lower() == 'yes':
        play_again = True
        print()
    elif play_again.lower() == 'no':
        play_again = False
        print()
        print('Thank you. Goodbye.')


# start here
print()
print('Welcome in the game "Rock, Paper and Scissors"')
print()

play_again = True
while play_again:
    game()