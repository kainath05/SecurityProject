def block_encrypt(plaintext: bytes, key: bytes, block_size: int) -> bytes:
    # Padding directly in the encrypt method
    padding_length = block_size - (len(plaintext) % block_size)
    padded_plaintext = plaintext + bytes([padding_length] * padding_length)

    # XOR operation directly in the encrypt method
    ciphertext = b""
    for i in range(0, len(padded_plaintext), block_size):
        block = padded_plaintext[i:i + block_size]
        xor_result = bytes(a ^ b for a, b in zip(block, key))
        ciphertext += xor_result

    return ciphertext

def block_decrypt(ciphertext: bytes, key: bytes, block_size: int) -> bytes:
    # XOR operation directly in the decrypt method
    plaintext = b""
    for i in range(0, len(ciphertext), block_size):
        block = ciphertext[i:i + block_size]
        xor_result = bytes(a ^ b for a, b in zip(block, key))
        plaintext += xor_result

    # Unpadding directly in the decrypt method
    padding_length = plaintext[-1]
    unpadded_plaintext = plaintext[:-padding_length]

    return unpadded_plaintext
