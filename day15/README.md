<h1 align="center">☕ Coffee Machine – Python Terminal App</h1>

<p align="center">
  A terminal-based drink ordering simulation in Python.<br>
  Insert coins, manage balance, and enjoy espresso, latte, or cappuccino!
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=flat-square&logo=python">
  <img src="https://img.shields.io/badge/Project-Type%3A-Terminal_App-lightgrey?style=flat-square">
  <img src="https://img.shields.io/badge/Status-Completed-brightgreen?style=flat-square">
</p>

---

<h2>🎮 Game Preview</h2>

> Launch the script in your terminal and enjoy an interactive vending simulation.  
> Includes resource management, balance handling, admin menu, and live feedback.

---

<h2>📋 Features</h2>

- ✅ Interactive drink menu (espresso, latte, cappuccino)
- ✅ Coin-based payment system (quarters, dimes, nickles, pennies)
- ✅ Balance tracking + auto-change calculation
- ✅ Resource management for milk, water, and coffee
- ✅ Maintenance system with password (refill, report, shutdown)
- ✅ Cross-platform screen clearing
- ✅ Modular function-based structure

---

<h2>🧠 How to Use</h2>

1. Run the Python script
2. Choose a drink from the menu
3. Insert coins when prompted
4. Enjoy your drink or access system menu if low on resources
5. Play until you're done (or power off the machine)

---

<h2>🔐 Maintenance System</h2>

> If ingredients run out, you're prompted to access the system menu:

- Type `y` when prompted  
- Enter password: `4529`  
- Actions Available:
  - Refill water, milk, coffee
  - View current machine resources
  - Shut down the machine

---



<h2>🚀 Getting Started</h2>

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/coffee-machine.git

# 2. Navigate into the project folder
cd coffee-machine

# 3. Run the script
python coffee_machine.py
```

<h2> 🛠️ Requirements </h2>
Python 3.10 or higher

- No external libraries required

<h2>📁 Project Structure</h2>

```bash
coffee-machine/
├── coffee_machine.py     # Main Python script
└── README.md             # Documentation file
```

<h2>🎯 Future Improvements</h2>

- GUI version with tkinter
- Save logs and balances to a file
- Add new drinks (mocha, americano, etc.)
- Unit testing with unittest or pytest