# TODO-1: Import and print the logo from art.py when the program starts.
from art import logo


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# TODO-2: What happens if the user enters a number/symbol/space?

print(logo)
print(f"{'*'*50}\nWelcome to Caesar Cipher!\n{'*'*50}")

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1
    for letter in original_text:
        if letter in alphabet:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
        else:
            output_text+=letter
    print(f"Here is the {encode_or_decode}d result: {output_text}")


# TODO-3: Can you figure out a way to restart the cipher program?
Exit = False
while not Exit:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    Flag = True
    while Flag:
        try:
            shift = int(input("Type the shift number:\n"))
            Flag = False
        except ValueError:
            print("Error....you have entered a non integer value!")
            continue
    caesar(original_text=text,shift_amount=shift,encode_or_decode=direction)
    ask_user = input("to continue encrypting enter \"y\" to exit program enter \"n\": ").lower().strip()
    if ask_user == 'n':
        Exit = True
        print(f"{'*'*50}\ngoodbye  shutting system down.....\n{'*'*50}")




