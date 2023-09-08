from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def off_coffee_machine():
    print('Coffee machine off')
    exit()


menu_obj = Menu()
coffee_maker_obj = CoffeeMaker()
money_machine_obj = MoneyMachine()


while True:
    user_choose = input(f'What would you like? ({menu_obj.get_items()}): ').lower()

    if user_choose == 'off':
        off_coffee_machine()
    elif user_choose == 'report':
        coffee_maker_obj.report()
        money_machine_obj.report()
        continue

    drink_obj = menu_obj.find_drink(user_choose)
    if drink_obj is None:
        continue
    else:  # if drink is on menu
        is_enough_resourses = coffee_maker_obj.is_resource_sufficient(drink_obj)
        if is_enough_resourses:
            print(f'{drink_obj.name} cost ${drink_obj.cost}'.capitalize())
            payment_success = money_machine_obj.make_payment(drink_obj.cost)
            if payment_success:
                coffee_maker_obj.make_coffee(drink_obj)






