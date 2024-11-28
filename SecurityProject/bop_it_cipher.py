def bop_it_cipher_encrypt(text, twist_count, pull_count, bop_count):
    actions = ['twist'] * twist_count + ['pull'] * pull_count + ['bop'] * bop_count
    result = []
    for i, char in enumerate(text):
        action = actions[i % len(actions)]
        if char.isalpha():
            if action == 'twist':  # adds one to the shift
                new_char = chr((ord(char) + 1 - ord('a')) % 26 + ord('a')) if char.islower() else chr(
                    (ord(char) + 1 - ord('A')) % 26 + ord('A'))
            elif action == 'pull':  # subtracts one to the shift
                new_char = chr((ord(char) - 1 - ord('a')) % 26 + ord('a')) if char.islower() else chr(
                    (ord(char) - 1 - ord('A')) % 26 + ord('A'))
            elif action == 'bop':  # adds 3 to the shift
                new_char = chr((ord(char) + 3 - ord('a')) % 26 + ord('a')) if char.islower() else chr(
                    (ord(char) + 3 - ord('A')) % 26 + ord('A'))
            result.append(new_char)
        else:
            result.append(char)
    return ''.join(result)


def bop_it_cipher_decrypt(text, twist_count, pull_count, bop_count):
    actions = ['twist'] * twist_count + ['pull'] * pull_count + ['bop'] * bop_count
    result = []
    for i, char in enumerate(text):
        action = actions[i % len(actions)]
        if char.isalpha():
            if action == 'twist':
                new_char = chr((ord(char) - 1 - ord('a')) % 26 + ord('a')) if char.islower() else chr(
                    (ord(char) - 1 - ord('A')) % 26 + ord('A'))
            elif action == 'pull':
                new_char = chr((ord(char) + 1 - ord('a')) % 26 + ord('a')) if char.islower() else chr(
                    (ord(char) + 1 - ord('A')) % 26 + ord('A'))
            elif action == 'bop':
                new_char = chr((ord(char) - 3 - ord('a')) % 26 + ord('a')) if char.islower() else chr(
                    (ord(char) - 3 - ord('A')) % 26 + ord('A'))
            result.append(new_char)
        else:
            result.append(char)
    return ''.join(result)
