# Part 1: Check if a single number is prime
print("--- Prime Number Checker ---")
num = int(input("Enter an integer to check: "))

is_prime = True
if num <= 1:
    is_prime = False
else:
    # Check all numbers from 2 up to num - 1
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break  # Stop checking if we find a factor

if is_prime:
    print(f"{num} is a prime number.\n")
else:
    print(f"{num} is NOT a prime number.\n")


# Part 2: Find all primes within a user range
print("--- Prime Number Range Finder ---")
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

print(f"Prime numbers between {start} and {end}:")

# Loop through every number in the range
for current_num in range(start, end + 1):
    if current_num > 1:
        # Check if the current number has any factors
        has_factor = False
        for i in range(2, current_num):
            if current_num % i == 0:
                has_factor = True
                break
        
        # If no factors were found, it's prime
        if not has_factor:
            print(current_num, end=" ")
print() # Print a new line at the end
