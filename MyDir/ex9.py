# Here's some new strange stuff, remember to type it in correctly

days = "Mon Tue Wed Thu Fri Sat Sun"


# If we want to write multiple lines using only one print statement
# we can use the \n formatter which stands for "new line"
months = "\nJan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print("Here are the days: ", days)
print("Here are the months: ", months)

# If we want to include the "\n" in our print we have to use %r
# which prints out the raw text
print("Here are the months: %r " % months)



print(""" 
There's something going on here
With the three double quotes
We'll be able to type as much as we like.
Even 4 lines if we want, or 5 or 6.
""")