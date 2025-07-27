import random
import time
from art import logo
import os

def compare_number(user_guess,selected_number,turns):
    if user_guess < selected_number:
        print("Too low.\nGuess again.")
        return turns - 1
    elif user_guess > selected_number:
        print("Too high.\nGuess again.")
        return turns - 1
    else:
        print(f"You got it! The answer was {selected_number}.")

def set_difficulty():
    while True:
        game_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower().strip()
        if game_level == 'easy':
            no_of_turns = 10
            return no_of_turns
        elif game_level == 'hard':
            no_of_turns = 5
            return no_of_turns
        else:
            print("That was an invalid input!")


#after we specified the chances now we enter the game loop
def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    number = random.randint(1, 100)
    print("I'm thinking of a number between 1 and 100.")
    no_of_chances = set_difficulty()
    guess = ""
    while no_of_chances > 0:
        while True:
            try:
                guess = int(input(f"You have {no_of_chances} attempts remaining to guess the number.\nMake a guess: "))
                break
            except ValueError:
                print("You entered a non valid input!")
        no_of_chances = compare_number(guess,number,no_of_chances)
        if guess == number:
            break
    if guess != number:
        print(f"You've run out of guesses. Refresh the page to run again.")

continue_playing = True
while continue_playing:
    game()
    while True:
        ask_user = input("Do you want to play again?(y/n): ").lower().strip()
        if ask_user == 'y':
            break
        elif ask_user == 'n':
            continue_playing = False
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Closing Game")
            for _ in range(3):
                print('.',end = '')
                time.sleep(0.5)
            print("Goodbye!")
            time.sleep(1)
            break
        else:
            print("That was an invalid input!")
