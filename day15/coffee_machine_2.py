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
'quarters' :0,
'dimes' : 0,
'nickles': 0,
'pennies': 0,
}

resources ={
    "water": 300,
    "milk": 200,
    "coffee": 100,
}



def print_report():
    print(f"water: {str(resources['water'])}\n:milk: {str(resources['milk'])}\ncoffee: {str(resources['coffee'])}\nMoney: {YOUR_MONEY}")

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
    resources["water"] +=300
    resources["coffee"] +=100



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
    total_money+= inserted_money["quarters"] * 0.25
    total_money+=inserted_money["dimes"] * 0.01
    total_money+=inserted_money["nickles"]*0.05
    total_money+=inserted_money["pennies"] *0.01
    return total_money
        
#we are going to make a coffee machine
def coffee_machine():
    print(logo)
    print(f"{'*'*50}\nWelcome to Coffee Machine!\n{'*'*50}")
    machine_is_on = True
    while machine_is_on:
        prompt = input("What would you like?\n1.espresso\n2.latte\n3.capuccino\n4.report\nchoose an option: ").lower().strip()
        chosen_option = user_input_conversion(prompt)
        drinks = ['espresso','latte','capuccino']
        if chosen_option in drinks:
            if check_sufficient_resources(chosen_option):
                drink_price = MENU[chosen_option]["cost"]
                if YOUR_MONEY >= drink_price:
                    pay_money()
                    payed_money = process_money()
                    YOUR_MONEY-=payed_money
                    if payed_money > drink_price:
                        change = payed_money - drink_price
                        print(f"Your change is: {change}")
                        YOUR_MONEY += change
                else:
                    print("Sorry the amount of money you have is not sufficient for this drink.")
            else:
                print(f"the resources in the coffee machine: water: {str(resources['water'])}\n"
                f"milk: {str(resources['milk'])}\ncoffee: {str(resources['coffee'])}")
                print("the resources in the machine is not sufficient, reffiling the system",end="")
                for _ in range(4):
                    time.sleep(1)
                    print(".",end = "")

        elif chosen_option == 'report':
            print_report()
        elif chosen_option == 'off':
            print("Turning the machine off",end='')
            machine_is_on = False
            for _ in range(3):
                print('.',end = "")
                time.sleep(0.5)
            os.system('cls' if os.name == 'nt' else 'clear')

coffee_machine()