# Accept an uppercase character from the user
user_input = input("Enter an uppercase letter (A-Z): ").strip()

# Validate that the input is exactly one uppercase letter
if len(user_input) == 1 and user_input.isupper() and user_input.isalpha():
    # Subtract 65 (ASCII value of 'A') to make A = 0
    numerical_value = ord(user_input) - 65
    
    print(f"The numerical representation of '{user_input}' is {numerical_value}")
else:
    print("Invalid input! Please enter a single uppercase letter from A to Z.")
