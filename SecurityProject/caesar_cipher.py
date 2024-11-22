def caesar_cipher_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                new_char = chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a'))
            elif char.isupper():
                new_char = chr((ord(char) - ord('A') + shift_amount) % 26 + ord('A'))  # needed since it thinks of
                # upper case characters are different
            result += new_char
        else:
            result += char  # non-alphabetical characters are just added as is
    return result


def menu_option_1():
    text = input("Enter the text to encrypt: ")

    while True:
        shift_input = input("Enter the number of positions to shift: ")
        if shift_input.isdigit():
            shift = int(shift_input)
            break
        else:
            print("Invalid input. Please enter a number.")

    encrypted_text = caesar_cipher_encrypt(text, shift)
    print(f"Encrypted text: {encrypted_text}")