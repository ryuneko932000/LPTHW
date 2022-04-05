# Reading files


# Importing necessary libraries and variable declaration
from sys import argv 
script, filename = argv

# Declaring txt is the opened file we want to inspect
txt = open(filename)

# Printing the name of our file and the contents of it 
# by using .read()
print(f"Here's your file: {filename}")
print(txt.read())


# Same thing is done here just with another name.
print ("Type the filename again:")
file_again = input("> ")
txt_again = open(file_again)
print(txt_again.read())


# We close now the files as we don't need them anymore.
txt.close()
txt_again.close()