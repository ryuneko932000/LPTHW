# Names, variables, code, functions


# unlimited args
def print_two(*args):
	arg1, arg2 = args
	print(f"arg1: {arg1} , arg2: {arg2}")
	
# only two args
def print_two_again(arg1, arg2):
	print(f"arg1: {arg1} , arg2: {arg2}")
	
# only one argument
def print_one(arg1):
	print(f"arg1: {arg1}")
	
# no arguments
def print_none():
	print("No arguments given")

print_two("Sebas", "Ricardo")
print_two_again("Sebas", "Ricardo")
print_one("First!")
print_none()