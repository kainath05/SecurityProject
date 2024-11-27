def encrypt_transposition(plaintext, key):
    # Remove spaces from plaintext
    plaintext = plaintext.replace(" ", "")
    
    # Determine the number of columns
    num_columns = len(key)
    
    # Create a grid to hold the plaintext
    grid = [""] * num_columns  # One string for each column
    
    # Fill the grid column by column
    for i, char in enumerate(plaintext):
        column = i % num_columns  # Cycle through columns
        grid[column] += char
    
    # Rearrange columns based on the key
    sorted_key = sorted((char, idx) for idx, char in enumerate(key))
    ciphertext = ""
    for _, col_idx in sorted_key:
        ciphertext += grid[col_idx]
    
    return ciphertext


def decrypt_transposition(ciphertext, key):
    # Determine the number of columns
    num_columns = len(key)
    
    # Determine the number of rows
    num_rows = len(ciphertext) // num_columns
    remainder = len(ciphertext) % num_columns
    
    # Calculate the column lengths
    column_lengths = [num_rows + (1 if col < remainder else 0) for col in range(num_columns)]
    
    # Split the ciphertext into columns based on key order
    sorted_key = sorted((char, idx) for idx, char in enumerate(key))
    columns = []
    start = 0
    for _, col_idx in sorted_key:
        length = column_lengths[col_idx]
        columns.append(ciphertext[start:start+length])
        start += length
    
    # Rebuild the original grid based on the unsorted key
    unsorted_key = sorted(range(len(key)), key=lambda idx: key[idx])
    original_columns = [columns[idx] for idx in unsorted_key]
    
    # Rebuild the plaintext by reading row by row
    plaintext = ""
    for row in range(num_rows + (1 if remainder > 0 else 0)):
        for col in range(num_columns):
            if row < len(original_columns[col]):
                plaintext += original_columns[col][row]
    
    return plaintext
