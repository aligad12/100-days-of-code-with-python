import string
import random

letters = list(string.ascii_letters)
numbers = list(string.digits)
symbols = list(string.punctuation)
#now we have all the letters,numbers and symbols, we now can start to make our password generator
num_letters = int(input("please enter the number of letters you want: "))
num_symbols = int(input("please enter the numbers of symbols you want: "))
num_numbers = int(input("please enter the number of digits you want: "))
rand_numbers = [random.choice(numbers) for number in range(num_numbers)]
rand_symbols =[random.choice(symbols) for symbol in range(num_symbols)]
rand_letters = [random.choice(letters) for letter in range(num_letters)]
print(f"the random numbers generated are: \n{rand_numbers}"
      f"\nthe random symbols generated are: \n{rand_symbols}"
      f"\nthe random letters generated are: \n{rand_letters}")
my_pass = []
my_pass.extend(rand_numbers)
my_pass.extend(rand_symbols)
my_pass.extend(rand_letters)

random.shuffle(my_pass)
new_password = ''.join(my_pass)
print(new_password)