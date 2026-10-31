# Caesar Cipher - fixed shift of 3

def encrypt(text):
    result = ""
    for ch in text:
        if ch.isupper():
            result += chr((ord(ch) - ord('A') + 3) % 26 + ord('A'))
        elif ch.islower():
            result += chr((ord(ch) - ord('a') + 3) % 26 + ord('a'))
        else:
            result += ch
    return result

def decrypt(text):
    result = ""
    for ch in text:
        if ch.isupper():
            result += chr((ord(ch) - ord('A') - 3) % 26 + ord('A'))
        elif ch.islower():
            result += chr((ord(ch) - ord('a') - 3) % 26 + ord('a'))
        else:
            result += ch
    return result

message = input("Enter the message: ")
encrypted = encrypt(message)

print("Encrypted:", encrypted)
print("Decrypted:", decrypt(encrypted))
