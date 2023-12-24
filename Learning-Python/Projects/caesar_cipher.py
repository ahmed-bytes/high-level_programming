"""Encrypts and decrypts coded message."""
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
]


def encrypt(message, points):
    encrypt_text = ""
    for letter in message:
        alpha_index = alphabet.index(letter)
        if (alpha_index + shift) > 25:
            alpha_index = 0
        alpha_index += points
        new_letter = alphabet[alpha_index]
        encrypt_text += new_letter
    return encrypt_text


def decrypt(message, points):
    decrypt_text = ""
    for letter in message:
        alpha_index = alphabet.index(letter)
        if ((alpha_index - points) - 1) < 0:
            new_letter = alphabet[alpha_index]
            decrypt_text += new_letter
        else:
            alpha_index -= points
            new_letter = alphabet[alpha_index]
            decrypt_text += new_letter
    return decrypt_text


print("Welcome To Caecasr Cipher v2.0..")
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

print(encrypt(message=text, points=shift))
print(decrypt(message=text, points=shift))
