# Shift Cipher - Encrypt and Decrypt

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

print("Encrypted:", encrypt(message, key))
print("Decrypted:", decrypt(encrypt(message, key), key))
