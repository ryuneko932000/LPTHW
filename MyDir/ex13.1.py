# Combining argv and input()


from sys import argv
script, color, adjective = argv

animal = input("Type in your favorite animal")

print("So you have a %s %s %s in your room, what do you do?"
		
	  % (adjective, color, animal))