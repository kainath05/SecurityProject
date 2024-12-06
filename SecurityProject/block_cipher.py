def block_encrypt(plaintext: bytes, key: bytes, block_size: int, rounds: int = 12) -> bytes:
    # Padding
    padding_length = block_size - (len(plaintext) % block_size)
    padded_plaintext = plaintext + bytes([padding_length] * padding_length)

    ciphertext = padded_plaintext
    for _ in range(rounds):
        temp_ciphertext = b""
        for i in range(0, len(ciphertext), block_size):
            block = ciphertext[i:i + block_size]
            xor_result = bytes(a ^ b for a, b in zip(block, key))
            temp_ciphertext += xor_result
        ciphertext = temp_ciphertext
    return ciphertext


def block_decrypt(ciphertext: bytes, key: bytes, block_size: int, rounds: int = 12) -> bytes:
    plaintext = ciphertext
    for _ in range(rounds):
        temp_plaintext = b""
        for i in range(0, len(plaintext), block_size):
            block = plaintext[i:i + block_size]
            xor_result = bytes(a ^ b for a, b in zip(block, key))
            temp_plaintext += xor_result
        plaintext = temp_plaintext

    # Unpadding
    padding_length = plaintext[-1]
    unpadded_plaintext = plaintext[:-padding_length]
    return unpadded_plaintext
