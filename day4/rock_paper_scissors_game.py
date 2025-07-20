import random

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
draws = [rock,paper,scissors]
flag = True
#making the rock paper scissors game now:
while flag:
    try:
        user = int(input("enter 0 for rock, 1 for paper, 2 for scissors: "))
    except ValueError:
        print("you entered a non integer value!")
        continue
    possible_solutions = [0,1,2]
    if user not in possible_solutions:
        print("Sorry, this is an invalid input!")
    else:
        print(f"user picked: \n {draws[user]}")
        choices = ["rock","paper","scissors"]
        computer = random.choice(possible_solutions)
        print(f"computer picked \n {draws[computer]}")
        computer = choices[computer]
        user = choices[user]
        if user == computer:
            print("Tie")
        elif user == "rock" and computer == "scissors":
            print("you win!")
        elif user == "paper" and computer == "rock":
            print("you win!")
        elif user == "scissors" and computer == "paper":
            print("you win!")
        else:
            print("you lose!")
        flag = False

        #you can apply a simpler logic here instead of that







