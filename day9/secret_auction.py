# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
#now we try to create the secret auction program by ourselves without the help of any one
logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
import os


print(logo)
print(f"{'*'*50}\nWelcome to Secret Auction App!\n{'*'*50}")
def secret_auction():
    still_bidding = True
    bidding_list = {}
    max_value = 0
    while still_bidding:
        name = input("What is your name?: ")
        while True:
            try:
                bid = float(input("What is your bid? $"))
                break
            except ValueError:
                print("The value you entered is not a number.."
                      "\nPlease enter again.")
        bidding_list[name] = bid

        while True:
            ask_user = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower().strip()
            if ask_user == "no":
                still_bidding = False
                break
            elif ask_user == "yes":
                os.system('cls' if os.name == 'nt' else 'clear')
                print(logo)
                print(f"{'*'*50}\nYou are now bidding in Secret Auction App!\n{'*'*50}")
                break
            else:
                print("this was not a valid response!")
                continue
    name_of_highest_bid = ""
    for key in bidding_list:
        if bidding_list[key] > max_value:
            max_value = bidding_list[key]
            name_of_highest_bid = key
    print(f"The winner is {name_of_highest_bid} with a bid of ${max_value}")



secret_auction()

