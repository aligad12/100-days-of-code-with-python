<h1 align="center">🎮 Hangman Game</h1>

<p align="center">
<i>A classic <b>Python CLI game</b> where you guess letters<br>
to uncover a hidden word before the hangman is fully drawn!</i>
</p>

<p align="center">
<img src="https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python" alt="Python Badge" />
<img src="https://img.shields.io/badge/Game-Hangman-red?style=flat-square" alt="Hangman Badge" />
<img src="https://img.shields.io/badge/App-CLI-green?style=flat-square" alt="CLI Badge" />
</p>

---

## 🔐 Overview
This is a simple command-line Hangman game built with Python.
The player has to guess the hidden word one letter at a time.
If the player guesses incorrectly, they lose a life and the hangman drawing progresses.

---

## ✨ Features
- ASCII art for hangman stages
- Life tracking system (6 lives total)
- Letter-by-letter guessing
- Prevents repeated guesses
- Friendly command-line interface with feedback

---

## ⚙️ How to Run
```bash

#first you need to go to the directory where you installed the code file.
#use commands like:
#:D or :C based on where you downloaded the file
#then when you are in the directory containing the file you can run:
python hangman.py
```

---

## ⚖️ Rules
- You start with 6 lives
- Each wrong guess costs 1 life
- The game ends when the word is guessed or lives reach 0
- Already guessed letters are tracked

---

## 🖊️ Sample Output
```
 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    
 welcome to hangman game!
the word you are trying to guess is: ________
***********you have 6/6 lives *************
guess a letter: a
__a_____

  +---+
  |   |
      |
      |
      |
      |
=========

***********you have 6/6 lives *************
guess a letter: v
__a_____
the letter v is not in the word :(, you lose a life:

  +---+
  |   |
  O   |
      |
      |
      |
=========

***********you have 5/6 lives *************
guess a letter: e
__a___e_

  +---+
  |   |
  O   |
      |
      |
      |
=========

***********you have 5/6 lives *************
guess a letter: n
__a___e_
the letter n is not in the word :(, you lose a life:

  +---+
  |   |
  O   |
  |   |
      |
      |
=========

***********you have 4/6 lives *************
guess a letter: m
__a___e_
the letter m is not in the word :(, you lose a life:

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
***********you have 3/6 lives *************
guess a letter: s
__a___e_
the letter s is not in the word :(, you lose a life:

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========

***********you have 2/6 lives *************
guess a letter: d
__a___ed

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========

***********you have 2/6 lives *************
guess a letter: f
f_a___ed

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========

***********you have 2/6 lives *************
guess a letter: r
fra___ed

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========

***********you have 2/6 lives *************
guess a letter: y
fra___ed
the letter y is not in the word :(, you lose a life:

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========

***********you have 1/6 lives *************
guess a letter: n
fra___ed
you have already guessed this letter before!
***********you have 1/6 lives *************
guess a letter: k
fra___ed
the letter k is not in the word :(, you lose a life:
you lost...
the word was: frazzled

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
```

---

## 🚀 Future Improvements
- Add word difficulty levels
- Add a scoreboard or win counter
- Fetch words from an API or file

---

## 📚 License
This project is open-source and free to use for educational or personal purposes.
