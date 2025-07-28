<h1 align="center">🤫 Secret Auction Program</h1>

<p align="center">
<i>A terminal-based blind auction application built with Python.<br>
Collect bids secretly and reveal the highest bidder at the end!</i>
</p>

<p align="center">
<img src="https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python" alt="Python Badge" />
<img src="https://img.shields.io/badge/Project-Fundamentals-orange?style=flat-square" alt="Fundamentals Badge" />
<img src="https://img.shields.io/badge/App-CLI-green?style=flat-square" alt="CLI Badge" />
</p>

---

## 🔒 Overview

This Secret Auction program was built as a hands-on exercise to apply fundamental Python concepts — focusing on data handling, control flow, and user interaction in the terminal.

The application simulates a blind auction process where:

- Participants enter their names and secret bids.
- The console is cleared between bids to maintain secrecy.
- After all bids are collected, the program determines and announces the highest bidder.

---

## ✨ Features

- 🖼️ **ASCII logo** for app flair (displayed in the terminal)  
- 💰 **Secret Bidding**: Bids are hidden from other participants  
- 👥 **Multiple Bidders**: Supports any number of participants  
- 🏆 **Highest Bidder Determination**: Automatically identifies the winner  
- ✅ **Input Validation**: Ensures bids entered are valid numbers  
- 🔁 **Re-run Option**: Allows users to easily start a new auction after one concludes  
- 🧹 **Clean UI**: Clears the screen between bids for a smooth user experience  

---

## 🚀 Getting Started

To get this Secret Auction running on your local machine, follow these steps:

### ✅ Prerequisites

You'll need Python installed on your system. Download it from [python.org](https://www.python.org).

### 💻 Installation & Execution

```bash
# 1. Clone the repository (if using Git)
git clone <repository_url>
cd secret-auction-program

# OR just save the Python file manually as:
# secret_auction.py

# 2. Run the program
python secret_auction.py
```

Follow the on-screen prompts to enter bidder names and their secret bids.

---

## 🗃️ Project Structure

```bash
secret-auction-program/
├── secret_auction.py   # Main game logic
├── README.md           # You're here!
```

---

## 🖥️ Program Output Example

```
**************************************************
Welcome to Secret Auction App!
**************************************************
What is your name?: Alice
What is your bid? $150
Are there any other bidders? Type 'yes' or 'no'.
yes

**************************************************
You are now bidding in Secret Auction App!
**************************************************
What is your name?: Bob
What is your bid? $180
Are there any other bidders? Type 'yes' or 'no'.
yes

**************************************************
You are now bidding in Secret Auction App!
**************************************************
What is your name?: Charlie
What is your bid? $120
Are there any other bidders? Type 'yes' or 'no'.
no
The winner is Bob with a bid of $180.00
Would you like to run another auction? (yes/no): no
Thank you for using the Secret Auction App! closing app . . . .
goodbye...
```

---

## 💡 How the Code Works

### 🧾 `bidding_list` (dictionary)

The main data structure for storing bids:

```python
bidding_list = {
    "Alice": 150.00,
    "Bob": 180.00,
    "Charlie": 120.00
}
```

### 🎨 `logo`

A multi-line string holding ASCII art for the auction logo, displayed at the start and between rounds. (Defined in your Python code.)

### 🔁 `secret_auction()` Function

- Orchestrates the bidding process.
- Uses a `while` loop to collect names and bids.
- Includes input validation via `try-except`.
- Clears the console using:

```python
os.system('cls' if os.name == 'nt' else 'clear')
```

- Calls `get_highest_bidder()` after all bids are entered.

### 🏆 `get_highest_bidder(bidding_list)` Function

- Iterates through the dictionary to find the highest bid.
- Displays the winner and bid amount.

### 🔄 Main Program Flow

- Starts with `secret_auction()`.
- Outer `while using_app:` loop allows multiple auctions.
- Prompts user to restart or exit.

---

## 🌐 Live Demo (Run it Online!)

You can run this project in your browser using [Replit](https://replit.com):

1. Go to [Replit.com](https://replit.com), and log in or sign up.
2. Create a new Repl and choose **Python**.
3. Paste the code from `secret_auction.py` into the editor.
4. Click **Run**, and interact with your program directly in the console.

---

## 👨‍💻 Author

Made with 💻 and 🧠 by **Ali Gad**  
A capstone project from my Python learning journey, focusing on functions, logic, user input, and clean CLI design.

---

## 🤝 Contributing

This project is a personal learning exercise. However, if you have suggestions or find any issues, feel free to open an issue or submit a pull request!

---

## 📄 License

This project is open-source and available under the [MIT License](https://opensource.org/licenses/MIT).
