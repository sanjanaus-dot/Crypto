#final block is padded with X.
text= input("Enter a string: ")

# Loop through the string in steps of 5
for i in range(0, len(text), 5):
    chunk = text[i:i+5]
    
    # Pad with 'X' if the chunk is shorter than 5 characters
    padded_chunk = chunk.ljust(5, 'X')
    
    print(padded_chunk)
