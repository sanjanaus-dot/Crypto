# Rail Fence Cipher Encryption

message = input("Enter the message: ").replace(" ", "")
rails = int(input("Enter the number of rails: "))

if rails < 2:
    print("Number of rails must be at least 2.")
else:
    # Create an empty pattern with the required number of rails.
    fence = [["" for column in range(len(message))]
             for row in range(rails)]

    row = 0
    direction = 1

    # Write letters in a zigzag pattern.
    for column in range(len(message)):
        fence[row][column] = message[column]

        if row == 0:
            direction = 1
        elif row == rails - 1:
            direction = -1

        row = row + direction

    # Read the letters row by row to get the encrypted message.
    encrypted = ""

    for row in range(rails):
        for column in range(len(message)):
            encrypted = encrypted + fence[row][column]

    print("Encrypted message:", encrypted)
