#!/usr/bin/python3
# Exercise 19 - Functions and Variables

# Define the function that will be run.
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("That's enough for a party!")
    print("Get a blanket.\n")

# Run the function while passing the aguments as integers in the brackets.
print("We can just give the function numbers directly:")
cheese_and_crackers(50,20)

# State variables that can be passed as arguments in the function.
print("Or, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 20

# Arithmetic used to pass as arguments for the function.
print("We can even do math inside:")
cheese_and_crackers(10 + 20, 5 + 7)

# The following arithmetic will be reduced to 2 separate integers which are
# passed as arguments.
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
