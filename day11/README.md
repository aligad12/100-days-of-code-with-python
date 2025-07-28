<h1 align="center">🃏 Blackjack – Capstone Project</h1>

<p align="center">
  <i>A terminal-based card game built with Python.<br>
  Test your luck, strategy, and decision-making — can you beat the dealer without going bust?</i>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=flat-square&logo=python" alt="Python Badge" />
  <img src="https://img.shields.io/badge/Project-Capstone-orange?style=flat-square" alt="Capstone Badge" />
  <img src="https://img.shields.io/badge/Game-Type--CLI-green?style=flat-square" alt="CLI Badge" />
</p>

---

## 🎮 Gameplay Overview

> This Blackjack game was built as a **capstone project** to apply Python fundamentals — using logic, functions, and user interaction in the terminal.

🂠 The game simulates a simplified version of Blackjack where:
- The **player** and **computer dealer** are dealt cards.
- The player can **draw or hold**.
- The dealer draws until reaching a score of 17+.
- Whoever gets closer to **21** without going over **wins**.

---

## ✨ Features

- 🖼️ **ASCII logo** for game flair  
- 🃏 Dynamic **card drawing** for player and dealer  
- 🅰️ Smart **Ace handling** (1 or 11)  
- 🧠 Dealer uses basic Blackjack strategy  
- 🔁 Game restart loop with clean UI  
- ❌ Bust detection and win/loss logic  
- 🎯 Real-time card reveals and suspense  

---

## 🚀 Getting Started

```bash
# 1. Clone the repo
git clone https://github.com/yourusername/blackjack-capstone.git

# 2. Move into the folder
cd blackjack-capstone

# 3. Run the game
python main.py

---

## 🗃️ Project Structure

```bash
blackjack-capstone/
├── main.py         # Game logic
├── art.py          # ASCII banner/logo
├── README.md       # You're here!

---
## 🧠 Card Deck Logic
The game simulates a minimal deck using this structure:
```bash
cards = {
  "Ace": [1, 11],
  "normal": [2, 3, 4, 5, 6, 7, 8, 9, 10],
  "K": 10,
  "Q": 10,
  "J": 10
}
---
-Ace values are chosen interactively by the player when needed.
---

## 👨‍💻 Author
-Made with 💻 and 🧠 by Ali Gad
-A capstone project from my Python learning journey, focusing on functions, logic, user input, and clean CLI design.