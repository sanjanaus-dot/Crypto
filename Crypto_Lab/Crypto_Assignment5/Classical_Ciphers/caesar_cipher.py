# Caesar Cipher - Encryption and Decryption
# Caesar cipher is a shift cipher with a fixed key of 3.

KEY = 3


def encrypt(text):
    result = ""
    for ch in text:
        if ch.isupper():
            result += chr((ord(ch) - ord('A') + KEY) % 26 + ord('A'))
        elif ch.islower():
            result += chr((ord(ch) - ord('a') + KEY) % 26 + ord('a'))
        else:
            result += ch
    return result


def decrypt(text):
    return encrypt_with_key(text, -KEY)


def encrypt_with_key(text, key):
    result = ""
    for ch in text:
        if ch.isupper():
            result += chr((ord(ch) - ord('A') + key) % 26 + ord('A'))
        elif ch.islower():
            result += chr((ord(ch) - ord('a') + key) % 26 + ord('a'))
        else:
            result += ch
    return result


message = input("Enter the message: ")
encrypted = encrypt(message)
print("Encrypted message:", encrypted)
print("Decrypted message:", decrypt(message) if False else encrypt_with_key(encrypted, -KEY))
