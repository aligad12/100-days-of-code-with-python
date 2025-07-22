import random

gallow = """
  +---+
  |   |
      |
      |
      |
      |
=========
"""
Head = """
  +---+
  |   |
  O   |
      |
      |
      |
========="""
Body = """
  +---+
  |   |
  O   |
  |   |
      |
      |
========="""
one_arm = """ 
  +---+
  |   |
  O   |
 /|   |
      |
      |
========="""
both_arms = """
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
"""
one_leg = """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
========="""
both_legs ="""
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========="""
body_parts = [gallow,Head,Body,one_arm,both_arms,one_leg,both_legs]

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
place_holders = []
for char in chosen_word:
    place_holders.append("_")
size = len(place_holders)
guessed_letter = input("guess a letter: ").lower()
counter = 0

def reveal_hang_man_word(word,size,letter):
    if len(word) != size:
        raise ValueError
    else:
        word_as_list = list(word) #hawelna el word de le list 3shan nethakem ahsan
        for i in range(len(word)):
            if word_as_list[i] == letter:
                place_holders[i] = letter
    return "".join(place_holders)


while "".join(place_holders) != chosen_word:
    if guessed_letter in chosen_word:
        reveal_hang_man_word(chosen_word,size,guessed_letter)
        guessed_word = "".join(place_holders)
        print(guessed_word)
    else:
        print("wrong guess!")
        print(body_parts[counter])
        counter+=1
        if counter == len(body_parts):
            print("you lost!")
            break
    if guessed_word == chosen_word:
        print("you won!")
        break
    else:
        guessed_letter = input("guess a letter: ").lower()






