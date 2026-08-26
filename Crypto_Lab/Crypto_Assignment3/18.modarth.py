# Accept an integer from the user
try:
    user_input = int(input("Enter an integer: "))
    
    # Calculate integer modulo 26
    result = user_input % 26
    
    # Display the result
    print(f"{user_input} mod 26 = {result}")

except ValueError:
    print("Invalid input! Please enter a valid integer.")
