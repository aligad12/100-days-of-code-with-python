from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


is_machine_on = True
drinks = ['latte','espresso','cappuccino']
coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()
my_menu = Menu()
while is_machine_on:
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower().strip()
    if user_input == 'off':
        is_machine_on = False
    elif user_input == "report":
        coffee_machine.report()
    elif user_input in drinks:
        the_drink = my_menu.find_drink(user_input)
        if coffee_machine.is_resource_sufficient(the_drink):
            make_payment = money_machine.make_payment(the_drink.cost)
            if make_payment:
                coffee_machine.make_coffee(the_drink)
    elif user_input == 'refill':
        coffee_machine = CoffeeMaker()
    else:
        print("That was an invalid input!")

