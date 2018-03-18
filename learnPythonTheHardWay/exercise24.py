#!/usr/bin/python3

print("Let's practise everytihng.")
print('You would need to know \'bout escapes with \ that do:')
print('\n newlines and \t tabs.')

poem = """
\tLine1
line2
line3
line4
\n\t\tsame
"""


print("-----")
print(poem)
print("-----")

five = 10 - 2 + 3 - 6
print(f"This variable is equal to five: {five}")

def secret_formula(started):
    jelly_beans = started* 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return int(jelly_beans), int(jars), int(crates)

start_point = 10000
beans, jars, crates = secret_formula(start_point)

print("With a starting point of: {}".format(start_point))

print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("We can also do that this wya:")
formula = secret_formula(start_point)

print("We would have {} beans, {} jars, and {} crates.".format(*formula))

