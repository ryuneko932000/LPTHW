# More Practice
print("Let's practice everything.")
print('You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.')

poem = """
\tThe lovely world
with logic so firmly planted 
cannon discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation.
\n\t\twhere the is none.
"""

divider = '____________'
print(divider)
print(poem)
print(divider)


five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000 
    crates = jars / 100 
    return jelly_beans, jars, crates

start_point = 100000
jelly_beans, jars, crates = secret_formula(start_point)

print(f"With a starting point of: {start_point}")
print(f"We'd have {jelly_beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("We'd also do that this way:")
print(f"We'd have {jelly_beans} beans, {jars} jars, and {crates} crates.  ")