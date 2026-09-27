# Brute-Force Attack on Shift Cipher

cipher = "MCI RWR WH"

print("Cipher text:", cipher)
print("\nAll 26 possible plaintexts:")

for key in range(26):
    plaintext = ""

    for char in cipher:
        if char.isalpha():
            # Try shifting each letter backwards by the key.
            value = (ord(char) - 65 - key) % 26
            plaintext = plaintext + chr(value + 65)
        else:
            plaintext = plaintext + char

    print("Key", key, ":", plaintext)
