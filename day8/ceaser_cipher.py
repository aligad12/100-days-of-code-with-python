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
print(logo)
print("welcome to ceaser cipher: ")
def encrypt(entered_word,shifting_number):
    new_word = []
    word_length = len(entered_word)
    for i in range(word_length):
        letter= entered_word[i]
        if letter.isalpha():
            base = ord('A') if letter.isupper() else ord('a')
            shifted = chr((ord(letter)-base +shifting_number) % 26 + base) #+base el fl akher deh 3shan neraga3 el arkam lel asl msh el mapping el 3amalnah
            new_word.append(shifted)
        else:
            new_word.append(letter)
    return "".join(new_word)

def decrypt(entered_word,shifting_number):
    new_word = []
    word_length = len(entered_word)
    for i in range(word_length):
        letter = entered_word[i]
        if letter.isalpha():
            base = ord('A') if letter.isupper() else ord('a')
            shifted = chr((ord(letter) - base - shifting_number) % 26 + base)
            new_word.append(shifted)
        else:
            new_word.append(letter)
    return "".join(new_word)

encrypting = True
close_program = False
decrypting = True
while not close_program:
    try:
        option = int(input("menu:\n1.encrypt\n2.decrypt\n3.close program\nchoose an option: "))
    except ValueError:
        print("you entered a non integer Value")
        continue

    if option == 1:
        encrypting = True
        while encrypting:
            word=input("enter the word you want to encrypt: ")
            shifting_value = int(input("enter the shifting value required to encrypt your message: : "))
            print(f"the encrypted word for {word} is :{encrypt(word,shifting_value)}")
            decision = input("do you want to continue encrypting messages?(y,n): ")
            if decision.lower().strip() == "n":
                encrypting = False

    elif option == 2:
        decrypting = True
        while decrypting:
            word=input("enter the word you want to decrypt: ")
            shifting_value = int(input("enter the shifting value required to decrypt your message: "))
            print(f"the decrypted word for {word} is: {decrypt(word,shifting_value)}")
            decision = input("do you want to continue decrypting messages?(y,n): ")
            if decision.lower().strip() == "n":
                decrypting = False
    elif option == 3:
        print("Goodbye....shutting down")
        break