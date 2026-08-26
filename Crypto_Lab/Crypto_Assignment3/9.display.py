message = "CRYPTOLOGY USING PYTHON"

#convert to lowercase;
print("Lowercase:", message.lower())

#convert to uppercase;
print("Uppercase:", message.upper())

#check whether "PYTHON" exists in the string;
#1print("Does 'PYTHON' exist in the string?", "PYTHON" in message)

# Check existence
if "PYTHON" in message:
    print("Yes, 'PYTHON' exists in the string.")
else:
    print("No, 'PYTHON' does not exist.")

#replace "PYTHON" with "PROGRAMMING".
print("After replacing 'PYTHON' with 'PROGRAMMING':", message.replace("PYTHON", "PROGRAMMING"))