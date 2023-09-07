from data import MENU, resources


def exit_func():
    print('Machine off')
    exit()


def bad_input_from_user():
    print('I don\'t know this command. Sorry')
    # break


def report_func():
    print(f'Water: {resources["water"]}')
    print(f'Milk: {resources["milk"]}')
    print(f'Coffee: {resources["coffee"]}')
    print(f'Money: ${resources["money"]}')


def check_resources(drink):
    for ingredient in MENU[drink]['ingredients']:
        if resources[ingredient] - MENU[drink]['ingredients'][ingredient] < 0:  # when not enought resourses
            print(f'Sorry there is not enough {ingredient}.')
            return False
    return True  # if enough resourses


def process_coins(drink):
    print('Please insert coins')
    twenty_five = input('How many quarters (25)?: ')
    ten = input('How many dimes (10)?: ')
    five = input('How many nickles (5)?: ')
    one = input('How many pennies (1)?: ')

    try:
        total = int(twenty_five) * 0.25 + int(ten) * 0.1 + int(five) * 0.05 + int(one) * 0.01
    except ValueError:
        print('You put bad coins')
    else:
        if total < MENU[drink]['cost']:
            print("Sorry that's not enough money. Money refunded.")
        else:  # if enough money or too many
            resources['money'] += MENU[drink]['cost']
            for ingredient in MENU[drink]['ingredients']:
                resources[ingredient] -= MENU[drink]['ingredients'][ingredient]

            if total > MENU[drink]['cost']:
                change = total - MENU[drink]['cost']
                print(f'Here is ${round(change, 2)} dollars in change.')

            print(f'Here is your {drink}. Enjoy!')


while True:
    user_choose = input('What would you like? (espresso/latte/cappuccino): ').lower()

    if user_choose == 'off':
        exit_func()
    elif user_choose == 'report':
        report_func()
    elif user_choose in ['espresso', 'latte', 'cappuccino']:
        is_enough_resources = check_resources(user_choose)
        if is_enough_resources:
            process_coins(user_choose)
    else:
        bad_input_from_user()
