# Simple Diffie-Hellman (DH) Key Exchange

# Public values (known to both users)
p = 23
g = 5

# Private keys (kept secret by each user)
a = 6
b = 15

# Public keys calculated by each user
A = pow(g, a, p)
B = pow(g, b, p)

print("DIFFIE-HELLMAN KEY EXCHANGE")
print("Public prime (p):", p)
print("Public base (g):", g)

print("\nUser 1 public key:", A)
print("User 2 public key:", B)

# Exchange public keys and calculate the shared secret
key_user1 = pow(B, a, p)
key_user2 = pow(A, b, p)

print("\nShared key calculated by User 1:", key_user1)
print("Shared key calculated by User 2:", key_user2)

if key_user1 == key_user2:
    print("Key exchange successful!")
else:
    print("Key exchange failed!")
