# Shift Cipher - Encryption and Decryption

def encrypt(text, key):
    result = ""
    for ch in text:
        if ch.isupper():
            result += chr((ord(ch) - ord('A') + key) % 26 + ord('A'))
        elif ch.islower():
            result += chr((ord(ch) - ord('a') + key) % 26 + ord('a'))
        else:
            result += ch
    return result


def decrypt(text, key):
    return encrypt(text, -key)


message = input("Enter the message: ")
key = int(input("Enter shift key: "))

encrypted = encrypt(message, key)
print("Encrypted message:", encrypted)
print("Decrypted message:", decrypt(encrypted, key))
