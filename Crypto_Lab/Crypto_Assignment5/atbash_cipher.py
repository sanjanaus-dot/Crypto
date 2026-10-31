# Atbash Cipher - A becomes Z, B becomes Y, and so on

def atbash(text):
    result = ""
    for ch in text:
        if ch.isupper():
            result += chr(ord('Z') - (ord(ch) - ord('A')))
        elif ch.islower():
            result += chr(ord('z') - (ord(ch) - ord('a')))
        else:
            result += ch
    return result

message = input("Enter the message: ")
encrypted = atbash(message)

print("Encrypted:", encrypted)
print("Decrypted:", atbash(encrypted))
