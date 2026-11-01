# Columnar Transposition: Encryption and Decryption

def encrypt(message, key):
    message = message.replace(" ", "")
    cols = len(key)
    rows = (len(message) + cols - 1) // cols
    grid = [["" for _ in range(cols)] for _ in range(rows)]

    pos = 0
    for r in range(rows):
        for c in range(cols):
            if pos < len(message):
                grid[r][c] = message[pos]
                pos += 1

    order = sorted(range(cols), key=lambda c: (key[c], c))
    cipher = ""
    for c in order:
        for r in range(rows):
            cipher += grid[r][c]
    return cipher


def decrypt(cipher, key):
    cols = len(key)
    rows = (len(cipher) + cols - 1) // cols
    extra = len(cipher) % cols

    lengths = []
    for c in range(cols):
        lengths.append(rows if extra == 0 or c < extra else rows - 1)

    order = sorted(range(cols), key=lambda c: (key[c], c))
    grid = [["" for _ in range(cols)] for _ in range(rows)]

    pos = 0
    for c in order:
        for r in range(lengths[c]):
            grid[r][c] = cipher[pos]
            pos += 1

    message = ""
    for r in range(rows):
        for c in range(cols):
            message += grid[r][c]
    return message


text = input("Enter plaintext: ").upper()
key = input("Enter key (letters): ").upper()

if not key.isalpha():
    print("Key must contain letters only.")
else:
    cipher = encrypt(text, key)
    print("Encrypted text:", cipher)
    print("Decrypted text:", decrypt(cipher, key))
