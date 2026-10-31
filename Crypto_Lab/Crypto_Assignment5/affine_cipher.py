# Affine Cipher - Encrypt and Decrypt
# Encryption: E(x) = (a*x + b) mod 26
# Decryption: D(x) = a_inverse*(x - b) mod 26

import math

def mod_inverse(a):
    for i in range(1, 26):
        if (a * i) % 26 == 1:
            return i
    return None

def encrypt(text, a, b):
    result = ""
    for ch in text:
        if ch.isupper():
            x = ord(ch) - ord('A')
            result += chr((a * x + b) % 26 + ord('A'))
        elif ch.islower():
            x = ord(ch) - ord('a')
            result += chr((a * x + b) % 26 + ord('a'))
        else:
            result += ch
    return result

def decrypt(text, a, b):
    inverse = mod_inverse(a)
    result = ""
    for ch in text:
        if ch.isupper():
            y = ord(ch) - ord('A')
            result += chr((inverse * (y - b)) % 26 + ord('A'))
        elif ch.islower():
            y = ord(ch) - ord('a')
            result += chr((inverse * (y - b)) % 26 + ord('a'))
        else:
            result += ch
    return result

message = input("Enter the message: ")
a = int(input("Enter key a (must be coprime with 26): "))
b = int(input("Enter key b: "))

if math.gcd(a, 26) != 1:
    print("Invalid key a. Choose a value coprime with 26, such as 1, 3, 5, 7, 9, 11.")
else:
    encrypted = encrypt(message, a, b)
    print("Encrypted:", encrypted)
    print("Decrypted:", decrypt(encrypted, a, b))
