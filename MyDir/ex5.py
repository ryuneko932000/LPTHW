# More variables and printing

my_name = 'Sebastian Macias'
my_age = 21
my_height = 72
my_weight = 176
my_eyes = 'Brown'
my_teeth = 'White'
my_hair = 'Brown'

print ("Let's talk about %s" % my_name)
print ("He's %d inches tall" % my_height)
print ("He's %d pounds heavy." % my_weight)
print ("Actually that's not so heavy.")
print("He's got %s eyes and %s hair." % (my_eyes, my_hair))
print ("His teeth are usually %s depending on the coffee." % my_teeth)

# this line was a bit tricky to write actually 
print ("If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)