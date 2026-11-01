# Double Columnar Transposition: Encryption and Decryption

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
key1 = input("Enter first key: ").upper()
key2 = input("Enter second key: ").upper()

if not key1.isalpha() or not key2.isalpha():
    print("Keys must contain letters only.")
else:
    first = encrypt(text, key1)
    second = encrypt(first, key2)
    print("Encrypted text:", second)

    undo_first = decrypt(second, key2)
    original = decrypt(undo_first, key1)
    print("Decrypted text:", original)
