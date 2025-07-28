# 🂡 Blackjack in Python

Welcome to **Blackjack**, a classic terminal-based card game where you challenge the dealer (computer) and aim to get a hand value as close to 21 as possible—without going over!

> 🎯 Are you feeling lucky?

---

## 🎮 Game Preview

A CLI-based card game that mimics the classic Blackjack experience:

```
The player cards: 10, Q
The computer cards: 4, ?
Do you want to deal? (y/n): y
You got an Ace, Do you want it as 1 or 11: 11
```

---

## 🧠 How to Play

* You and the computer start with 2 cards each
* Face cards (K, Q, J) are worth 10
* Aces can be 1 or 11 depending on your choice
* Your goal: reach 21 or get closer than the computer
* If your score goes over 21, you **Bust**

---

## 📦 Features

✅ ASCII-art Blackjack logo
✅ Random card draw logic with real-like values
✅ Smart Ace handling: choose between 1 or 11
✅ Dealer auto-deals until 17+
✅ Full game logic: busts, ties, and winner announcement
✅ Clean separation of logic in functions

---

## 🛠️ Setup Instructions

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/blackjack-python.git

# 2. Navigate into the folder
cd blackjack-python

# 3. Run the game
python main.py
```

> ✅ Requires Python 3.x

---

## 📁 Project Structure

```
blackjack-python/
├── main.py       # Main game logic
├── art.py        # Contains ASCII logo (optional)
├── README.md     # This file 😄
```

---

## 📌 Logic Highlights

* The dealer (computer) keeps drawing cards until they reach a score of 17 or more.
* The player can keep drawing as long as their score is under 21.
* Aces are smart! You're asked whether to count them as 1 or 11, and the computer makes smart choices automatically.

---

## 🚀 Example Card Logic

```python
cards = {
    "Ace": [1, 11],
    "normal": [2, 3, 4, 5, 6, 7, 8, 9, 10],
    "K": 10,
    "Q": 10,
    "J": 10
}
```

---

## 🙋 Author

Made with 🃏 and ☕ by **Ali G**

---

## 📜 License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

---

### 💬 Got suggestions or improvements?

Feel free to fork the repo and open a pull request!
