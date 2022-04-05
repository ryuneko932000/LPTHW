# Functions can return something

def add(a,b): 
	print(f"Adding {a} + {b}")
	return a + b
	
def substract(a,b):
	print(f"Substracting {a} - {b}")
	return a - b
	
def multiply(a,b):
	print(f"Multiplying {a} * {b}")
	return a * b

def divide(a,b):
	print(f"Dividing {a} / {b}")

print("Let's do some math with just functions!")

age = add(30, 5)
height = substract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

