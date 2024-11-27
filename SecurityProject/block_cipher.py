def block_encrypt(plaintext: bytes, key: bytes, block_size: int) -> bytes:
    # Add padding
    padding_length = block_size - (len(plaintext) % block_size)
    padded_plaintext = plaintext + bytes([padding_length] * padding_length)

    # XOR encryption
    ciphertext = b""
    for i in range(0, len(padded_plaintext), block_size):
        block = padded_plaintext[i:i + block_size]
        xor_result = bytes(a ^ b for a, b in zip(block, key))
        ciphertext += xor_result

    return ciphertext


def block_decrypt(ciphertext: bytes, key: bytes, block_size: int) -> bytes:
    # XOR decryption
    plaintext = b""
    for i in range(0, len(ciphertext), block_size):
        block = ciphertext[i:i + block_size]
        xor_result = bytes(a ^ b for a, b in zip(block, key))
        plaintext += xor_result

    # Validate and remove padding
    padding_length = plaintext[-1]
    if padding_length < 1 or padding_length > block_size:
        raise ValueError("Invalid padding detected.")
    unpadded_plaintext = plaintext[:-padding_length]

    return unpadded_plaintext

