import os
import time

logo = r"""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""


print(logo)
def display_astricks():
    return '*'*50
def display_intro():
    print(f"{display_astricks()}\nWelcome to the calculator app!\n{display_astricks()}")

def addition(f_number,s_number):
    return f_number + s_number

def division(f_number,s_number):
    if s_number != 0:
        return f_number/s_number
    else:
        return ZeroDivisionError

def subtraction(f_number,s_number):
    return f_number - s_number

def multiplication(f_number,s_number):
    return f_number * s_number

def validate_input(prompt):
    while True:
        try:
            number = float(input(prompt))
            return number
        except ValueError:
            print("the value you entered was an invalid input, please enter again!")
            continue

def operation_validation():
    while True:
        user_selection = input("+\n-\n*\n/\nEnter the operation you want to do: ")
        if user_selection in ['-','*','/','+']:
            return user_selection
        else:
            print("This operation is invalid!")

def display_answer(first_number,second_number,answer,operation):
    return f"{first_number} {operation} {second_number} = {answer:.5f}"

def exit_option(history):
    options = ['1','2','3']
    while True:
        prompt = input("\n1. Continue calculations\n2. View History\n3. Exit app.\nselection: ").strip()
        if prompt in options:
            if prompt == '1':
                flag =  False
                break
            elif prompt == '2':
                display_history(history)
            else:
                flag = True
                break
        else:
            print("This entry is not in the menu\nHere is the menu again.\n")
    return flag

def display_history(history):
    for calculation in history:
        print(calculation, end = " : ")
        print(history[calculation])



def calculator_app():
    exit_app = False
    display_intro()
    old_calculations = {}
    counter = 1
    while not exit_app:
        first_number = validate_input("Enter the first number for your operation: ")
        user_option = operation_validation()
        second_number = validate_input("Enter the second number for your operation: ")
        if user_option == '*':
            answer = multiplication(first_number,second_number)
        elif user_option == '/':
            answer = division(first_number,second_number)
        elif user_option == '+':
            answer = addition(first_number,second_number)
        else:
            answer = subtraction(first_number,second_number)
        print(display_answer(first_number,second_number,answer,user_option))
        old_calculations[counter] = display_answer(first_number, second_number, answer, user_option)
        counter+=1
        exit_app = exit_option(history=old_calculations)
        if exit_app == True:
            os.system('cls' if os.name== 'nt' else 'clear')
            print("Exiting Calculator")
            for i in range(3):
                time.sleep(0.5)
                print(".",end=" ")
            print("goodbye!")
            time.sleep(1)


calculator_app()



