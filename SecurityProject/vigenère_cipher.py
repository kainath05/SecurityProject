def vigenere_cipher_encrypt(msg, key):
    encrypted_text = []
    key = list(key)
    key_length = len(key)

    for i in range(len(msg)):
        char = msg[i]
        if char.isupper():
            encrypted_char = chr((ord(char) + ord(key[i % key_length]) - 2 * ord('A')) % 26 + ord('A'))
        elif char.islower():
            encrypted_char = chr((ord(char) + ord(key[i % key_length]) - 2 * ord('a')) % 26 + ord('a'))
        else:
            encrypted_char = char
        encrypted_text.append(encrypted_char)

    return ''.join(encrypted_text)  # convert the result list to a string and return it


def vigenere_cipher_decrypt(msg, key):
    decrypted_text = []
    key = list(key)
    key_length = len(key)

    for i in range(len(msg)):
        char = msg[i]
        if char.isupper():
            decrypted_char = chr((ord(char) - ord(key[i % key_length]) + 26) % 26 + ord('A'))
        elif char.islower():
            decrypted_char = chr((ord(char) - ord(key[i % key_length]) + 26) % 26 + ord('a'))
        else:
            decrypted_char = char  # non-alphabetical characters are added as-is
        decrypted_text.append(decrypted_char)

    return ''.join(decrypted_text)
