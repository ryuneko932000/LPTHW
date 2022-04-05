# Reading and writing files
# Python functions are important, remember the following:
# close(), read(), readline(), truncate(), write()

from sys import argv
script, filename = argv

print(f"We're going to erase {filename}")
print("To proceed press CTRL-C, to cancel hit return")

input("?")

print ("Opening the file...")
target = open(filename, 'r+')

print("Turcarting file, goodbye!")
target.truncate()

print("Now I'm going to need three lines, please write them.")
line1 = input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line 3: ")
print("I'm going to write these into the file")

target.write(f"{line1}\n{line2}\n{line3}\n ")


print("If you wish to read your newly edited document type y or n to exit.")
shouldRead = input("> ")
if shouldRead == 'y':
	print(target.read())
elif shouldRead == 'n':
	exit()
else: 
	print("Character invalid")
