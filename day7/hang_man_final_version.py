import random
from hangman_art import stages,logo
from hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
place_holder=""
lives = 6
print(f"{logo}\n welcome to hangman game!")
for i in range(word_length):
    place_holder+="_"
print(f"the word you are trying to guess is: {place_holder}")
found_letters = []
game_over = False
guessed_letters = []

while not game_over:
    print(f"***********you have {lives}/6 lives *************")
    guess = input("guess a letter: ")
    display=""

    for letter in chosen_word:
        if letter == guess:
            display+=letter
            found_letters.append(letter)
        elif letter in found_letters:
            display+=letter
        else:
            display+="_"
    print(display)
    if guess in guessed_letters:
        print(f"you have already guessed this letter before!")
        continue
    else:
        guessed_letters.append(guess)
        if guess not in chosen_word:
            print(f"the letter {guess} is not in the word :(, you lose a life:")
            lives-=1
            if lives == 0:
                print("you lost...")
                game_over=True

    if "_" not in display:
        game_over = True
        print("You Win")
    print(stages[lives])
