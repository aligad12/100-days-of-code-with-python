import time
import os

logo = """
 _____        __  __           ___  ___           _     _             ______          ___  _ _   _____           _ 
/  __ \      / _|/ _|          |  \/  |          | |   (_)            | ___ \        / _ \| (_) |  __ \         | |
| /  \/ ___ | |_| |_ ___  ___  | .  . | __ _  ___| |__  _ _ __   ___  | |_/ /_   _  / /_\ \ |_  | |  \/ __ _  __| |
| |    / _ \|  _|  _/ _ \/ _ \ | |\/| |/ _` |/ __| '_ \| | '_ \ / _ \ | ___ \ | | | |  _  | | | | | __ / _` |/ _` |
| \__/\ (_) | | | ||  __/  __/ | |  | | (_| | (__| | | | | | | |  __/ | |_/ / |_| | | | | | | | | |_\ \ (_| | (_| |
 \____/\___/|_| |_| \___|\___| \_|  |_/\__,_|\___|_| |_|_|_| |_|\___| \____/ \__, | \_| |_/_|_|  \____/\__,_|\__,_|
                                                                              __/ |                                
                                                                             |___/                                 
"""

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
YOUR_MONEY = 0
inserted_money = {
    'quarters': 0,
    'dimes': 0,
    'nickles': 0,
    'pennies': 0,
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def print_report():
    print(
        f"water: {str(resources['water'])}ml\n:milk: {str(resources['milk'])}ml\ncoffee: {str(resources['coffee'])}g\nMoney: ${YOUR_MONEY}")


def check_sufficient_resources(user_input):
    if user_input in MENU:
        if user_input == "espresso":
            if resources["water"] >= 50 and resources["coffee"] >= 18:
                return True
            else:
                return False
        elif user_input == "latte":
            if resources["water"] >= 200 and resources["coffee"] >= 24 and resources["milk"] >= 150:
                return True
            else:
                return False
        elif user_input == "cappuccino":
            if resources["water"] >= 250 and resources["coffee"] >= 24 and resources["milk"] >= 100:
                return True
            else:
                return False


def add_resources():
    """this function fills the machine with the same amount of the inital"""
    resources["milk"] += 200
    resources["water"] += 300
    resources["coffee"] += 100


def left_in_resources(drink):
    if "milk" in MENU[drink]["ingredients"]:
        if resources["milk"] < MENU[drink]["ingredients"]["milk"]:
            print("not enough milk")
    if resources["water"] < MENU[drink]["ingredients"]["water"]:
        print("not enough water")
    if resources["coffee"] < MENU[drink]["ingredients"]["coffee"]:
        print("not enough coffee")


def user_input_conversion(typed_message):
    if typed_message == '1' or typed_message == 'espresso':
        return "espresso"
    elif typed_message == '2' or typed_message == 'latte':
        return "latte"
    elif typed_message == '3' or typed_message == 'capuccino':
        return "capuccino"
    elif typed_message == '4' or typed_message == 'report':
        return "report"
    elif typed_message == 'off' or typed_message == 'close' or typed_message == 'shutdown':
        return 'off'
    else:
        return "That was an invalid input!"


def pay_money():
    print(f"The coins currency:\nquarters = $0.25\ndimes = $0.10\nnickles = $0.05\npennies = $0.01")
    no_quarters = float(input("insert coins to pay for your drink.\nHow many quarters do you want to insert: "))
    inserted_money["quarters"] += no_quarters
    no_pennies = float(input("How many pennies do you want to insert: "))
    inserted_money["pennies"] += no_pennies
    no_dimes = float(input("How many dimes do you want to insert: "))
    inserted_money["dimes"] += no_dimes
    no_nickles = float(input("How many nickles do you want to insert: "))
    inserted_money["nickles"] += no_nickles


def process_money():
    total_money = 0
    total_money += inserted_money["quarters"] * 0.25
    total_money += inserted_money["dimes"] * 0.01
    total_money += inserted_money["nickles"] * 0.05
    total_money += inserted_money["pennies"] * 0.01
    return total_money


def make_coffee(drink):
    if drink == "espresso":
        resources["water"] -= 50
        resources["coffee"] -= 18
    elif drink == "latte":
        resources["water"] -= 200
        resources["milk"] -= 150
        resources["coffee"] -= 24
    elif drink == "capuccino":
        resources["water"] -= 250
        resources["milk"] -= 100
        resources["coffee"] -= 24


def display_menu():
    print(f"Menu:\nespresso: $1.5\nlatte: $2.5\ncapuccino: $3.0")


def display_balance():
    global YOUR_MONEY
    print(f"Your balance now is: ${YOUR_MONEY}")


# we are going to make a coffee machine
def coffee_machine():
    password = "4529"
    global YOUR_MONEY
    print(logo)
    print(f"{'*' * 50}\nWelcome to Coffee Machine!\n{'*' * 50}")
    display_menu()
    machine_is_on = True
    while machine_is_on:
        prompt = input(
            "\n\nWhat would you like?\n1.espresso {$1.5}\n2.latte {$2.5}\n3.capuccino {$3.0}\n4.report\nchoose an option: ").lower().strip()
        chosen_option = user_input_conversion(prompt)
        drinks = ['espresso', 'latte', 'capuccino']
        if chosen_option in drinks:
            if check_sufficient_resources(chosen_option):
                drink_price = MENU[chosen_option]["cost"]
                print(f"The {chosen_option} costs: ${drink_price}")
                if YOUR_MONEY == 0:
                    print("You currently have no money in your balance.\n\n")
                    pay_money()
                    added_money = process_money()
                    YOUR_MONEY += added_money
                    display_balance()
                elif YOUR_MONEY >= drink_price:
                    payed_money = process_money()
                    YOUR_MONEY -= payed_money
                    if payed_money > drink_price:
                        change = payed_money - drink_price
                        print(f"Your change is: {change:.2f}")
                        YOUR_MONEY += change
                        display_balance()
                    make_coffee(chosen_option)
                    print(f"Here is your {chosen_option}! Have a niceday :)")
                else:
                    print("Sorry the amount of money you have is not sufficient for this drink.")
                    message = input("Do you want to add money now? (y/n):").lower().strip()
                    if message == 'y':
                        pay_money()
                        payed_amount = process_money()
                        YOUR_MONEY+=payed_amount
                        display_balance()
            else:
                print(f"the resources in the coffee machine:\nwater: {str(resources['water'])}ml\nmilk: {str(resources['milk'])}ml\ncoffee: {str(resources['coffee'])}g")
                print("the resources in the machine is not sufficient")
                maintenance_guy = input("Do you want to enter The system menu to refill the machine?").lower().strip()
                if maintenance_guy == 'y':
                    inside_system_menu = True
                else:
                    inside_system_menu = False
                counter = 3
                system_verification = ""
                while inside_system_menu:
                    if system_verification == "":
                        system_verification = input("If you are the maintenance, enter the password: ")
                    elif system_verification == "4529":
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print(logo)
                        print("Access granted")
                        check =  input("System Menu:\n1.Refill System.\n2.Turn Machine OFF.\n3.Exit System Menu\nchoose 1 or 2 or 3: ").lower().strip()
                        if check == '1':
                            print("Adding resources, This might take a while.",end = "")
                            for _ in range(6):
                                time.sleep(1)
                                print('.',end="")
                            add_resources()
                            temp = input("resources was added successfully.\n1.Exit Back to System Menu.\n2.Print a report for the Machine resources.\n:").lower().strip()
                            if temp == '1' :
                                continue
                            elif temp == '2' :
                                print(f"the resources in the coffee machine:\nwater: {str(resources['water'])}ml\nmilk: {str(resources['milk'])}ml\ncoffee: {str(resources['coffee'])}g")
                        elif check == '2':
                            print("Turning the machine off", end='')
                            machine_is_on = False
                            break
                        elif check == '3':
                            os.system('cls' if os.name == 'nt' else 'clear')
                            break
                    else:
                        if counter == 0:
                            print("no more chances!")
                            break
                        else:
                            print(f"That was a wrong password, you have {counter} more chances.")
                            counter -= 1
        if machine_is_on == False:
            break


        elif chosen_option == 'report':
            print_report()
        elif chosen_option == 'off':
            print("Turning the machine off", end='')
            machine_is_on = False
            for _ in range(3):
                print('.', end="")
                time.sleep(0.5)
            os.system('cls' if os.name == 'nt' else 'clear')


coffee_machine()