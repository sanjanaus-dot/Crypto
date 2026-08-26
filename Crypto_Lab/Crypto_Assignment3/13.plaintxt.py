#Read a message from the user 
message = input("Enter a message: ")

#remove leading/trailing spaces;
print("Removing leading/trailing spaces:", message.strip())

#convert it to uppercase;
print("Converting to uppercase:", message.upper())

#remove spaces between words.
print("Removing spaces between words:", message.replace(" ", ""))

