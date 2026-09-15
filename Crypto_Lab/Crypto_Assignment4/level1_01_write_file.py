# Accept five statements and store them in cryptology.txt

with open("cryptology.txt", "w") as file:
    for i in range(5):
        statement = input("Enter statement " + str(i + 1) + ": ")
        file.write(statement + "\n")

print("Statements saved in cryptology.txt")
