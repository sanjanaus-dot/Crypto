# User inputs
b = int(input("Enter the integer (b): "))
m = int(input("Enter the modulus (m): "))

inverse = None

# Brute force check: try every number from 1 up to m-1
for x in range(1, m):
    if (b * x) % m == 1:
        inverse = x
        break  # Found it, stop the loop

# Display results
if inverse is not None:
    print(f"\nThe multiplicative inverse of {b} mod {m} is: {inverse}")
    print(f"Verification: ({b} * {inverse}) mod {m} = {(b * inverse) % m}")
else:
    print(f"\nThe multiplicative inverse of {b} mod {m} does not exist.")
