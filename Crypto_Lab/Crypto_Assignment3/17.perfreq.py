text = input("Enter a string: ")

# Remove spaces to count only alphabetic characters
clean_text = text.replace(" ", "")
total_characters = len(clean_text)

# Calculate frequencies manually
frequency = {}
for char in clean_text:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

# Display header
print(f"Total Characters (excluding spaces): {total_characters}\n")
print(f"{'Character':<10} | {'Frequency':<10} | {'Percentage Frequency':<20}")
print("-" * 50)

# Calculate percentage and display results
for char in sorted(frequency.keys()):
    count = frequency[char]
    percentage = (count / total_characters) * 100
    
    # FIX: Put the entire formatted string inside the curly braces
    formatted_char = f"'{char}'"
    print(f"{formatted_char:<10} | {count:<10} | {percentage:.2f}%")
