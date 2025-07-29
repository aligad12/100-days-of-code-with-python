<h1 align="center">🔐 Caesar Cipher Program</h1>

<p align="center">
<i>A simple <b>Python CLI tool</b> to <b>encrypt</b> or <b>decrypt</b> messages<br>
using the classic <b>Caesar Cipher</b> technique.</i>
</p>

<p align="center">
<img src="https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python" alt="Python Badge" />
<img src="https://img.shields.io/badge/Project-Cipher-orange?style=flat-square" alt="Cipher Badge" />
<img src="https://img.shields.io/badge/App-CLI-green?style=flat-square" alt="CLI Badge" />
</p>

---

## 🔒 Overview

This **Caesar Cipher Program** is a straightforward **Python command-line interface (CLI) tool** designed to encrypt and decrypt text messages. It applies the traditional Caesar Cipher method, shifting each letter in a message by a specified number of positions in the alphabet.

The application allows you to:

* **Encrypt** any text with a chosen shift value.
* **Decrypt** messages previously encrypted with the same shift.
* Preserves upper/lowercase and non-alphabetic characters.

---

## ✨ Features

* ✅ **Encrypt & Decrypt:** Transform any word or sentence using a custom shift value.
* ✅ **Case-Preserving:** Maintains original uppercase and lowercase lettering.
* ✅ **Special Character Handling:** Non-alphabetic characters (like spaces, numbers, and punctuation) remain unchanged.
* ✅ **Interactive Menu:** A clean, easy-to-use menu guides you through the encryption/decryption process.
* 🖼️ **ASCII Art Banner:** Enjoy a stylish ASCII art display on startup.
* 🔁 **Continuous Operation:** Option to continue encrypting/decrypting or return to the main menu after each action.

---

## 🧠 What is a Caesar Cipher?

The **Caesar Cipher** is one of the earliest and simplest encryption techniques. It's a substitution cipher where each letter in the plaintext is replaced by a letter some fixed number of positions down or up the alphabet. For example, with a shift of 3, 'A' becomes 'D', 'B' becomes 'E', and so on.

> 💡 **Tip:** The same shift number used for encryption **must** be used to decrypt the message correctly.

---

## 🚀 Getting Started

To get this Caesar Cipher program running on your local machine, follow these steps:

### ✅ Prerequisites

- Python 3.x installed.  
You can download it from [python.org](https://www.python.org).

### 💻 Installation & Execution

```bash
# 1. Save the Python file manually as:
main.py

# 2. Open terminal / command prompt and navigate to the folder:
cd your_project_folder

# 3. Run the program:
python main.py

```bash

caesar_cipher/
├── main.py           # The main Caesar Cipher script
└── README.md         # You're here!

```

## 🖥️ Program Output Example

```bash

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
welcome to ceaser cipher:

menu:
1.encrypt
2.decrypt
3.close program
choose an option: 1
enter the word you want to encrypt: hello world!
enter the shifting value required to encrypt your message: 3
the encrypted word for hello world! is :khoor zruog!
do you want to continue encrypting messages?(y,n): n

menu:
1.encrypt
2.decrypt
3.close program
choose an option: 2
enter the word you want to decrypt: khoor zruog!
enter the shifting value required to decrypt your message: 3
the decrypted word for khoor zruog! is: hello world!
do you want to continue decrypting messages?(y,n): n

menu:
1.encrypt
2.decrypt
3.close program
choose an option: 3
Goodbye....shutting down

```
---

## 💡 How the Code Works (Conceptual)

- A banner is displayed at the start using ASCII art.

- User chooses from 3 options: encrypt, decrypt, or exit.

- Depending on choice:

- The program shifts each letter in the input text by a custom value.

- It handles uppercase/lowercase letters and skips non-alphabetic characters.

- You can keep using the tool repeatedly until you choose to exit.

---

## 👨‍💻 Author

- Made with 💻 and 🧠 by Ali Ahmed Gad

## 🚀 Further Enhancements (Optional)
- Want to expand this program? You could:

- ✅ Add input validation for invalid or negative shift values.

- ✅ Allow command-line arguments for automation:
- python main.py --encrypt "hello" --shift 3

- ✅ Create a GUI version with Tkinter for beginners or visual users.

- ✅ Save encrypted messages to a file or clipboard for easy sharing.


