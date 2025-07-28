<h1 align="center">🔢 Number Guessing Game</h1>

<p align="center">
  <em>Think you're lucky (or smart) enough to guess the secret number?</em><br>
  This is a simple terminal-based Python game where you guess a number between 1 and 100.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Made%20with-Python-blue?style=flat-square&logo=python" alt="Python badge">
  <img src="https://img.shields.io/badge/Difficulty-Easy%20%2F%20Hard-yellow?style=flat-square" alt="Difficulty badge">
  <img src="https://img.shields.io/badge/Game-Type%3A%20CLI-lightgrey?style=flat-square" alt="CLI badge">
</p>

---

## 🎮 Gameplay Overview

> "I'm thinking of a number between 1 and 100... can you guess it?"

* Choose your difficulty: `easy` (10 guesses) or `hard` (5 guesses)
* Enter a number each round
* Get hints: "Too high" or "Too low"
* Try to guess it before you run out of chances!

---

## 🧠 Features

* ✅ Input validation (only accepts numbers)
* ✅ Two difficulty modes (easy/hard)
* ✅ Feedback for each guess (too high / too low)
* ✅ Tracks remaining attempts
* ✅ Option to replay without restarting the terminal
* ✅ Graceful exit with animation

---

## 🛠️ Getting Started

```bash
# Clone the repo
git clone https://github.com/yourusername/number-guessing-game.git

# Enter the project folder
cd number-guessing-game

# Run the game
python main.py
```

> ⚠️ Python 3.x required

---

## 🧾 Example Session

```bash
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
Choose a difficulty. Type 'easy' or 'hard': easy
You have 10 attempts remaining to guess the number.
Make a guess: 50
Too low.
Guess again.
...
You got it! The answer was 72.
```

---

## 📁 File Structure

```
number-guessing-game/
├── art.py         # Logo ASCII art
├── main.py        # Main game logic
└── README.md      # Project readme file
```

---

## 💡 Possible Enhancements

<details>
<summary>Click to see ideas</summary>

* [ ] Add leaderboard with high scores
* [ ] Show number history of past guesses
* [ ] Add sound using `playsound` or `winsound`
* [ ] Convert to GUI using `Tkinter`
* [ ] Add difficulty progression based on score

</details>

---

## 👨‍💻 Author

Built with 🧠 and ☕ by **Ali G**

[![GitHub](https://img.shields.io/badge/GitHub-Ali--G-black?style=flat-square\&logo=github)](https://github.com/yourusername)

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
