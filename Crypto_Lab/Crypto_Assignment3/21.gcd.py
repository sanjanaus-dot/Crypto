# Accept two integers from the user
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

# Keep copies of the original numbers for the final print statement
a = num1
b = num2

# Euclidean Algorithm to find GCD
while b != 0:
    a, b = b, a % b

gcd = a
is_coprime = (gcd == 1)

# Display results
print(f"\nGCD({num1}, {num2}) = {gcd}")
if is_coprime:
    print(f"Yes, {num1} and {num2} are COPRIME numbers.")
else:
    print(f"No, {num1} and {num2} are NOT coprime numbers.")
