# Using argv and input 

# Now in this exercise we want to get an input from the user and then print it back. 
# However, instead of using the string formatting of "%s" or so we are gonna use a new method
# as this method will probably be considered deprecated in python3.

# The new way of doing this is using the f formatter: print(f"Hello {name}")

from sys import argv

script, user_name = argv
prompt = "> "

print(f"Hi {user_name}, I'm the {script} script")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What type of computer do you have?")
computer = input(prompt)

print(f""" 
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer}. Nice!
	  """)


	  
