#Read a string and divide it into blocks of five characters
string = input("Enter a string: ")
for i in range(0, len(string), 5):
    print(string[i:i+5], end=" ")




