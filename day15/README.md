☕ Coffee Machine – Python Terminal App

A terminal-based coffee vending simulation built in Python.
Select your drink, insert coins, and enjoy a virtual espresso, latte, or cappuccino!

🚀 Features

✔ Interactive text-based menu
✔ Coin payment simulation with real-time balance
✔ Smart resource management (water, milk, coffee)
✔ Admin system with password-protected access
✔ Auto-change calculation and balance updates
✔ Cross-platform screen clearing for a clean UI

1. espresso   - $1.5
2. latte      - $2.5
3. cappuccino - $3.0
4. report     - machine status
5. off        - shut down the machine

🎮 Sample Run

$ python coffee_machine.py

**************************************************
Welcome to Coffee Machine!
**************************************************

Menu:
espresso: $1.5
latte: $2.5
capuccino: $3.0

What would you like?
1.espresso {$1.5}
2.latte {$2.5}
3.capuccino {$3.0}
4.report
choose an option: 2

The latte costs: $2.5
You currently have no money in your balance.

insert coins to pay for your drink.
How many quarters do you want to insert: 10
How many pennies do you want to insert: 0
How many dimes do you want to insert: 0
How many nickles do you want to insert: 0

Your balance now is: $2.5
Here is your latte! Have a nice day :)

🔐 System Maintenance Access

To enter system maintenance mode:
- Type 'y' when prompted after a resource error
- Enter password: 4529

Available actions:
1. Refill resources (milk, water, coffee)
2. Shut down the machine
3. View machine report

🛠️ Requirements

- Python 3.10 or higher
- No external libraries required

📁 Project Structure

coffee_machine/
├── coffee_machine.py     # Main Python script
└── README.md             # This documentation

🎯 Future Improvements

- GUI support using tkinter or PySimpleGUI
- Save balance and transactions to a file
- Add more drink types and ingredients
- Implement unit testing with unittest

👨‍💻 Author

Ali G.
GitHub: https://github.com/yourusername
bash
Copy
Edit
📄 License

This project is open-source under the MIT License.
https://opensource.org/licenses/MIT