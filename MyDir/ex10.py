# What was that?

# When writing a string we can use the character "\" to type in formatters, an example of this 
# would be the new line formatter "\n", however there are even more formatters, such as "\\"
# which in this case prints a single "\". There are multiple formatters. Some of them are:



# print("I am 6'2" tall.")
# If we were to run the code above, we would get a syntax error, to circumvent this we need 
# to use the \ formatter. Using this we can escape double-quotes.
print("I am 6'2\" tall.")

tabby_cat = "\tI'm tabbed in"
persian_cat = "I'm split\non a line."
backlash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat Food
\t* Fishies
\t* Catnip\n\t* Grass 
          """
          
fatter_cat = '''
The other list for the fatter cat:
\t* Tuna cans
\t* Overloaded catnip
\t* Cuddles
			 '''
          
print(tabby_cat)
print(persian_cat)
print(backlash_cat)
print(fat_cat)
print(fatter_cat)
