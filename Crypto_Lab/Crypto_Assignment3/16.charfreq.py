#calculate the frequency of each character.

text = input("Enter a string: ")

# Dictionary to store character frequencies
frequency = {}

# Calculate frequency of each character (excluding spaces)
for char in text:
    if char != " ":
        frequency[char] = frequency.get(char, 0) + 1

# Identify the most frequently occurring character
most_frequent_char = max(frequency, key=frequency.get)
highest_count = frequency[most_frequent_char]

# Print the results
print("Character Frequencies:")
for char, count in sorted(frequency.items()):
    print(f"'{char}': {count}")

print(f"\nMost frequently occurring character: '{most_frequent_char}' (appears {highest_count} times)")
