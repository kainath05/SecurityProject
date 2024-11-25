import string
import random


def generate_key():
    letters = string.ascii_lowercase
    shuffled = ''.join(random.sample(letters, len(letters)))
    return {letter: shuffled[index] for index, letter in enumerate(letters)}


def monoalphabetic_cipher_encrypt(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                result += key[char]
            else:
                result += key[char.lower()].upper()
        else:
            result += char
    return result


def monoalphabetic_cipher_decrypt(text, key):
    reversed_key = {value: key for key, value in key.items()}
    result = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                result += reversed_key[char]
            else:
                result += reversed_key[char.lower()].upper()
        else:
            result += char
    return result
