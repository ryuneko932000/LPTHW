# Better version for exercise 17

from sys import argv
from os.path import exists

script, from_file, to_file = argv


print(f"Copying data from {from_file} to {to_file}")

# Original code (new one is way shorter): 
# in_file = open(from_file)
# indata = in_file.read()

indata = open(from_file).read()

print(f"The file {from_file} is {len(from_file)} bytes long")
print("Does the output file exist?")
print(f"> {exists(to_file)}")
print("Ready! Hit RETURN TO CONTINUE, CTRL-C TO ABORT")
input("> ")

out_file = open(to_file, 'w')
out_file.write(indata)

print("Done")
out_file.close()