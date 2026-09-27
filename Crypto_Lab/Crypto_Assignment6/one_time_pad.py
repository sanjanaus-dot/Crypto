# One Time Pad Encryption and Decryption

def encrypt(message, key):
    result = ""
    key_index = 0

    for char in message.upper():
        if char.isalpha():
            value = (ord(char) - 65 + ord(key[key_index]) - 65) % 26
            result = result + chr(value + 65)
            key_index = key_index + 1
        else:
            result = result + char

    return result


def decrypt(cipher, key):
    result = ""
    key_index = 0

    for char in cipher.upper():
        if char.isalpha():
            value = (ord(char) - 65 - (ord(key[key_index]) - 65)) % 26
            result = result + chr(value + 65)
            key_index = key_index + 1
        else:
            result = result + char

    return result


message = input("Enter the message: ").upper()
key = input("Enter the key (same number of letters as the message): ").upper()

# Count only letters because spaces and punctuation do not use key characters.
message_letters = sum(1 for char in message if char.isalpha())
key_letters = sum(1 for char in key if char.isalpha())

if message_letters != key_letters or not key.isalpha():
    print("Error: The key must contain exactly the same number of letters as the message.")
else:
    encrypted = encrypt(message, key)
    print("Encrypted message:", encrypted)

    decrypted = decrypt(encrypted, key)
    print("Decrypted message:", decrypted)
