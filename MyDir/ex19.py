# Functions and Variables
def fridge(sausages, eggs):
	print(f"You have {eggs} eggs! And {sausages} sausages!")
	
print("We can add numbers directly using the function")
fridge(20, 30)

print("Or we can use variables!")
num_sausages = 60
num_eggs = 50
fridge(num_sausages, num_eggs)

print("We can even do math inside the function too!")
fridge(30*2, 4+3)

print("And we can combine both variables and math!")
fridge(num_sausages + 2, num_eggs - 3)