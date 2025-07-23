alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.
# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.
# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.
# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?


def cryptography(original_text,shift_amount,decision):
    coded_word = ""
    for letter in original_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            if decision == 'encode':
                new_position = (position + shift_amount) % 26
                coded_letter = alphabet[new_position]
                coded_word += coded_letter
            elif decision =='decode':
                new_position = (position - shift_amount) % 26
                coded_letter = alphabet[new_position]
                coded_word += coded_letter
        else:
            coded_word+=letter # so this application here does not encrypt the symbols and the capital letters
            # it only handles the small letters to encrypt here
    return print(f"Here is the {'encrypted' if decision == 'encrypt' else 'decrypted' } result: {coded_word}")

print(logo)
print("***************************\nWelcome to caesar cipher!\n***************************")
exit = False
while not exit:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    while True:
        try:
            shift = int(input("Type the shift number:\n"))
            break
        except ValueError:
            print("you entered a non integer value.")
            continue
    cryptography(original_text=text,shift_amount=shift,decision=direction)
    choice = input("To continue crypto enter y to exit enter n: ").lower().strip()
    flag = True
    while flag:
        if choice == "n":
            exit=True
            flag = False
            print("shutting down, goodbye.....")
        elif choice == "y":
            flag = False
            continue
        else:
            print("you entered an invalid input!")









