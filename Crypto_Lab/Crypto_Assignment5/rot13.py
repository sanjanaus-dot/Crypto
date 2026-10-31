# ROT13 - shifts each letter by 13 places

def rot13(text):
    result = ""
    for ch in text:
        if ch.isupper():
            result += chr((ord(ch) - ord('A') + 13) % 26 + ord('A'))
        elif ch.islower():
            result += chr((ord(ch) - ord('a') + 13) % 26 + ord('a'))
        else:
            result += ch
    return result

message = input("Enter the message: ")
encrypted = rot13(message)

print("Encrypted:", encrypted)
print("Decrypted:", rot13(encrypted))
