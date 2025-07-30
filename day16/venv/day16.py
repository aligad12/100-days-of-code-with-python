from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


is_machine_on = True
coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()
drinks = ['latte','espresso','cappuccino']
while is_machine_on:
    user_drink = input("What would you like? (espresso/latte/cappuccino): ").lower().strip()
    if user_drink == 'off':
        is_machine_on = False
    elif user_drink == "report":
        coffee_machine.report()
    elif user_drink in drinks:
        the_drink = Menu.find_drink(user_drink)
        if coffee_machine.is_resource_sufficient(the_drink):
            payed_money = money_machine.process_coins()
            if money_machine.make_payment(the_drink.cost):
                coffee_machine.make_coffee(the_drink)
                print(f"Here is your {the_drink.name} ☕️!\nenjoy :)")


