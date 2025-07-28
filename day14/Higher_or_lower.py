from game_data import data
import random
from art import logo,vs
import time
import os

#list of dictionaries is the data
#the data is a list of dictionaries
def get_game_players():
    random_number = random.randint(0,len(data)-1)
    first_random_person = data[random_number]
    #but we want to exclude random number from it so we can make a while loop that check on it
    random_number_2 = random_number
    while random_number == random_number_2:
        random_number_2 = random.randint(0,len(data)-1)
    second_random_person = data[random_number_2]
    return first_random_person,second_random_person

def compare_persons(person1,person2,usr_answer):
    #since person 1 and person 2 are dictionaries so we want to get hold of the followers key and compare the values in it
    p1_followers = person1['follower_count']
    p2_followers = person2['follower_count']
    #usr_answer = A means person 1 and usr_answer = B means person 2
    if usr_answer == 'a':
        if p1_followers > p2_followers:
            return True
        elif p1_followers < p2_followers:
            return False
        else:
            print("Tie")
            return
    elif usr_answer == 'b':
        if p2_followers > p1_followers:
            return True
        elif p2_followers < p1_followers:
            return False
        else:
            print("Tie")
            return True
def game():
    streak = 0
    print(logo)
    print(f"{'*'*50}\nWelcome to Higher or Lower Game\n{'*'*50}")
    while True:
        first_player,second_player = get_game_players()
        print(f"compare A: {first_player['name']}, {first_player['description']}")
        print(vs)
        print(f"Against B: {second_player['name']}, {second_player['description']}")
        answer = ''
        while answer not in ['a','b']:
            answer = input("Who has more followers? Type 'A' or 'B' :").lower().strip()
        if compare_persons(first_player,second_player,answer):
            streak+=1
            print(f"You're right! Current score: {streak}")
        else:
            break
    print(f"Sorry, that's wrong. Final score: {streak}")

play_again = True
while play_again:
    game()
    prompt = input("Do you want to play again?(y/n): ").lower().strip()
    if prompt == 'n':
        play_again = False
        print("Exiting Game",end = "")
        for _ in range(3):
            print('.',end = "")
            time.sleep(0.5)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Goodbye!")
        time.sleep(0.5)
