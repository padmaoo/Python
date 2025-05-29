# Create a new file with the name 'sample.txt' 
    # - 'write' as separate execution 
    # - 'append & read' as separate execution

# Writing into a text file
with open('sample.txt', 'w') as file:
    file.write("This is the first line.\n")
    # Output --> Since, there is no file named as 'sample.txt'
               # it creates a new file naming 'sample.txt'
               # And writes 'This is the first line.' in the file.
    
# Appending and reading a file as a single execution 
with open('sample.txt', 'a+') as file:
    file.write("This is another appended line.\n")
    file.seek(0)  # Moves the cursor to the beginning of the file
    content = file.read() # Reads the content from the file
    print(content)
    # Output --> This is the first line.
               # This is another appended line.
