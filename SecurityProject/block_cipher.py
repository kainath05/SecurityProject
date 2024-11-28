import random
import string

def generate_key(block_size: int) -> bytes:
    """Generate a random key of the specified block size (in bytes)."""
    # Generate a random 64-bit key (if block_size is 8 bytes, we generate 64 bits)
    return bytes([random.randint(0, 255) for _ in range(block_size)])

def block_encrypt(plaintext: bytes, block_size: int, num_rounds: int = 12) -> bytes:
    """Encrypt the plaintext with multiple rounds using randomly generated keys."""
    # Add padding
    padding_length = block_size - (len(plaintext) % block_size)  # Find how much padding needs to be added
    padded_plaintext = plaintext + bytes([padding_length] * padding_length)

    # Encrypt in rounds
    ciphertext = padded_plaintext
    for round_num in range(num_rounds):
        # Generate a new random key for this round
        key = generate_key(block_size)

        # Perform XOR encryption for this round
        round_ciphertext = b""
        for i in range(0, len(ciphertext), block_size):
            block = ciphertext[i:i + block_size]
            xor_result = bytes(a ^ b for a, b in zip(block, key))
            round_ciphertext += xor_result

        ciphertext = round_ciphertext

    return ciphertext

def block_decrypt(ciphertext: bytes, block_size: int, num_rounds: int = 12) -> bytes:
    """Decrypt the ciphertext with multiple rounds using randomly generated keys."""
    # Decrypt in rounds
    plaintext = ciphertext
    for round_num in range(num_rounds):
        # Generate a new random key for this round
        key = generate_key(block_size)

        # Perform XOR decryption for this round
        round_plaintext = b""
        for i in range(0, len(plaintext), block_size):
            block = plaintext[i:i + block_size]
            xor_result = bytes(a ^ b for a, b in zip(block, key))
            round_plaintext += xor_result

        plaintext = round_plaintext

    # Validate and remove padding
    padding_length = plaintext[-1]
    if padding_length < 1 or padding_length > block_size:
        raise ValueError("Invalid padding detected.")
    unpadded_plaintext = plaintext[:-padding_length]

    return unpadded_plaintext
