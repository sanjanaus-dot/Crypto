# ROT13 Cipher - Encryption and Decryption
# ROT13 shifts every English letter by 13 positions.
# Applying ROT13 twice gives the original message.

def rot13(text):
    result = ""
    for ch in text:
        if 'A' <= ch <= 'Z':
            result += chr((ord(ch) - ord('A') + 13) % 26 + ord('A'))
        elif 'a' <= ch <= 'z':
            result += chr((ord(ch) - ord('a') + 13) % 26 + ord('a'))
        else:
            result += ch
    return result


message = input("Enter the message: ")
encrypted = rot13(message)
print("Encrypted message:", encrypted)
print("Decrypted message:", rot13(encrypted))
