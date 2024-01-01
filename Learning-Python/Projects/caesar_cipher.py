"""Encrypts and decrypts coded message."""
from ascii_art import caesar_art

alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    " ",
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    " ",
]


def caesar(direction, message, points):
    if direction == "encode":
        encrypt_text = ""
        for letter in message:
            if letter not in alphabet:
                encrypt_text += letter
            else:
                alpha_index = alphabet.index(letter)
                alpha_index += points
                new_letter = alphabet[alpha_index]
                encrypt_text += new_letter
        print(encrypt_text)
    elif direction == "decode":
        decrypt_text = ""
        for letter in message:
            if letter not in alphabet:
                decrypt_text += letter
            else:
                alpha_index = alphabet.index(letter)
                alpha_index -= points
                new_letter = alphabet[alpha_index]
                decrypt_text += new_letter
        print(decrypt_text)
    else:
        print("Command Error!!")


def prompt(response):
    if response == True or response == "okay" or response == "yes":
        return True
    else:
        return False


# Main code
print(caesar_art)
decision = True
print("Welcome To Caecasr Cipher v2.0..")

while decision == True:
    position = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

    caesar(direction=position, message=text, points=shift)

    choice = input("Do you want to go again!!: 'okay', 'yes'\n").lower()
    decision = prompt(choice)
