# Atbash Cipher - Encryption and Decryption
# Atbash replaces A with Z, B with Y, and so on.
# The same function is used for encryption and decryption.

def atbash(text):
    result = ""
    for ch in text:
        if 'A' <= ch <= 'Z':
            result += chr(ord('Z') - (ord(ch) - ord('A')))
        elif 'a' <= ch <= 'z':
            result += chr(ord('z') - (ord(ch) - ord('a')))
        else:
            result += ch
    return result


message = input("Enter the message: ")
encrypted = atbash(message)
print("Encrypted message:", encrypted)
print("Decrypted message:", atbash(encrypted))
