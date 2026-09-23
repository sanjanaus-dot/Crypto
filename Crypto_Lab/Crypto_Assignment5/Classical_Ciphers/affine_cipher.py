# Affine Cipher - Encryption and Decryption
# Encryption: E(x) = (a*x + b) % 26
# Decryption: D(y) = a_inverse * (y - b) % 26

from math import gcd

def mod_inverse(a, m):
    for number in range(1, m):
        if (a * number) % m == 1:
            return number
    return None


def encrypt(text, a, b):
    result = ""
    for ch in text:
        if 'A' <= ch <= 'Z':
            x = ord(ch) - ord('A')
            result += chr((a * x + b) % 26 + ord('A'))
        elif 'a' <= ch <= 'z':
            x = ord(ch) - ord('a')
            result += chr((a * x + b) % 26 + ord('a'))
        else:
            result += ch
    return result


def decrypt(text, a, b):
    inverse = mod_inverse(a, 26)
    result = ""
    for ch in text:
        if 'A' <= ch <= 'Z':
            y = ord(ch) - ord('A')
            result += chr((inverse * (y - b)) % 26 + ord('A'))
        elif 'a' <= ch <= 'z':
            y = ord(ch) - ord('a')
            result += chr((inverse * (y - b)) % 26 + ord('a'))
        else:
            result += ch
    return result


message = input("Enter the message: ")
a = int(input("Enter key a (must be coprime with 26): "))
b = int(input("Enter key b: "))

if gcd(a, 26) != 1:
    print("Invalid key! Choose a value of a that is coprime with 26.")
else:
    encrypted = encrypt(message, a, b)
    print("Encrypted message:", encrypted)
    print("Decrypted message:", decrypt(encrypted, a, b))
