# Simple RSA Algorithm (Educational Example)

# Two small prime numbers
p = 61
q = 53

# Calculate n and Euler's totient
n = p * q
phi = (p - 1) * (q - 1)

# Choose public key e
e = 17

# Calculate private key d
d = pow(e, -1, phi)

print("RSA ALGORITHM")
print("Public key:", (e, n))
print("Private key:", (d, n))

# Read the message
message = input("Enter a message: ")

# Encrypt each character
encrypted = []
for character in message:
    number = ord(character)
    encrypted.append(pow(number, e, n))

print("Encrypted message:", encrypted)

# Decrypt each number
decrypted = ""
for number in encrypted:
    character_number = pow(number, d, n)
    decrypted += chr(character_number)

print("Decrypted message:", decrypted)
