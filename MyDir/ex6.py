# Strings and Text


# Declaring variables with string formatting
x = "There are %d types of people" % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s" % (binary, do_not)


# When printing these variables, some variables get to pertain inside another
# thanks to the string formatting
print(x)
print(y)


# Again, these following print statements allow us to input a variable inside a variable
# inside another variable
print("I said: %r" % x) 
print ("I also said: '%s'" % y)


# Same case as the first example in this exercise, this time using boolean values
hilarious = False
joke_evaluation = "Isn't that joke so funny? %r"
print (joke_evaluation % hilarious)


# Print statements can also allow us to use certain variables and add them together.
w = "This is the left side of..."
e = "a string with a right side."

print(w+e)