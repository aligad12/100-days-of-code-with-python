from Tools.scripts.dutree import display
import random
logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

print(logo)
print(f"{'*'*50}\nWelcome to BlackJack game!\n{'*'*50}")
cards = {
    "Ace" : [1,11],
    "normal" : [2,3,4,5,6,7,8,9,10],
    "K" : 10,
    "Q" :10,
    "J" :10
}

def display_cards(pc_cards,user_cards):
    print("The player cards:",end = " ")
    for card in user_cards:
        print(card,end = ",")
    print("The computer cards are: ",end = " ")
    if sum(user_cards) < 21:
        for i in range(len(pc_cards)):
            if i == 0:
                print(pc_cards[0],end =",")
            else:
                print("?",end = ",")
    else:
        for card in pc_cards:
            print(card, end = ",")

def display_cards_end_game(pc_cards,user_cards):
    print("The player cards:",end = " ")
    for card in user_cards:
        print(card,end = ",")
    print("The computer cards are: ",end = " ")
    for i in range(len(pc_cards)):
            print(f"{pc_cards[i]}",end= ',')


def append_user_cards(cards):
    random_key = random.choice(keys)
    if random_key == "Ace":
        if sum(player_cards) < 11:
            temp = input("You got an Ace, Do you want it as 1 or 11: ").lower().strip()
            if temp == '1':
                random_card = 1
            elif temp == '11':
                random_card = 11
            else:
                random_card = 1 #if user typed something wrong or other thing.
        else:
            random_card = 1
    elif random_key == "normal":
        random_card = random.choice(cards[random_key])
    else:
        random_card = cards[random_key]
    return random_card

def default_cards_game_start(cards,keys,person_cards):
    random_key = random.choice(keys)
    if random_key == "Ace":
        if sum(person_cards) <11:
            random_card = 11
        else:
            random_card = 1
    elif random_key == "normal":
        random_card=  random.choice(cards[random_key])
    else:
        random_card = cards[random_key]
    return random_card

def check_wining_condition():
    if sum(player_cards) > 21:
        print("Bust!!!")
    elif sum(player_cards) <= 21 and sum(pc_cards) > 21:
        print("You win!")
    elif sum(player_cards) > sum(pc_cards):
        print("You win!")
    elif sum(player_cards) == sum(pc_cards):
        print("Tie")
    else:
        print("You lost")


def dealer_turn():
    pc_total = sum(pc_cards)
    while pc_total < 17:
        print("pc is dealing a card...")
        pc_cards.append(default_cards_game_start(cards,keys,pc_cards))
        pc_total = sum(pc_cards)

keys = ["Ace", "normal" , "K","Q","J"]
player_cards = []
pc_cards = []
player_cards.append(default_cards_game_start(cards,keys,player_cards))
pc_cards.append(default_cards_game_start(cards,keys,pc_cards))
player_cards.append(default_cards_game_start(cards,keys,player_cards))
pc_cards.append(default_cards_game_start(cards,keys,pc_cards))
display_cards(pc_cards=pc_cards,user_cards=player_cards)

while sum(player_cards) < 21:
    while True:
        deal_or_not = input("Do you want to deal? (y/n): ").lower().strip()
        if deal_or_not == 'y':
            player_cards.append(append_user_cards(cards))
            if sum(player_cards) < 21 and sum(pc_cards) != 21:
                continue
            else:
                break
        elif deal_or_not == 'n':
            break
    if deal_or_not == 'n':
        break
if sum(player_cards) <= 21:
    dealer_turn()

print("\n" + '*'*50)
display_cards_end_game(pc_cards,player_cards)
#check the winner then
print("\n" + '*'*50)
check_wining_condition()