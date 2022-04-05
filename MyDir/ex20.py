# Functions and files
from sys import argv

script, input_file = argv

def print_all(f):
	print(f.read())

def rewind(f):
	f.seek(0)


# To skip the blank lines use: ", end='' "
def print_a_line(line_count, f):
	print(line_count, f.readline(), end='')
	

current_file = open(input_file)

print("Print the whole file: \n")
print_all(current_file)

print("Rewinding...")
rewind(current_file)

print("Printing 3 lines:")
current_line = 1
print_a_line(current_line, current_file)
current_line += 1
print_a_line(current_line, current_file)
current_line += 1
print_a_line(current_line, current_file)