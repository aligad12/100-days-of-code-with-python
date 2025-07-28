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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def check_sufficient_resources(user_input):
    if user_input in MENU:
        if user_input == "espresso":
            if MENU[resources]["water"] >= 50 and MENU[resources]["coffee"] >= 18:
                return True
            else:
                return False
        elif user_input == "latte":
            if MENU[resources]["water"] >= 200 and MENU[resources]["coffee"] >= 24 and MENU[resources]["milk"] >= 150:
                return True
            else:
                return False
        elif user_input == "cappuccino":
            if MENU[resources]["water"] >= 250 and MENU[resources]["coffee"] >= 24 and MENU[resources]["milk"] >= 100:
                return True
            else:
                return False

def left_in_resources(drink):
    if "milk" in MENU[drink]:
        if MENU[resources]["milk"] < MENU[drink]["milk"]:
            print("not enough milk")
    if MENU[resources]["water"] < MENU[drink]["water"]:
        print("not enough water")
    if MENU[resources]["coffee"] < MENU[drink]["coffee"]:
        print("not enough coffee")


def user_input_conversion(typed_message):
    if typed_message == '1':
        return "espresso"
    elif typed_message == '2':
        return "latte"
    elif typed_message == '3':
        return "capuccino"
    elif typed_message == '4':
        return "report"
    else:
        return "that was an invalid input!"
#we are going to make a coffee machine
prompt = input("What would you like? 1.espresso\n2.latte\n3.capuccino\n4.report\nchoose an option: ").lower().strip()
if check_sufficient_resources(prompt):


if prompt == "report":
    print(f"Water: {MENU[resources]['Water']}\nMilk: {MENU[resources]['milk']}\nCofee: {MENU[resources]['coffee']}\nMoney: {money}")
