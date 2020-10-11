#!/usr/bin/python3
# Exercise 21 - Functions Can Return Something

def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"SUBTRACTING {a} + {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return int(a / b)


print("Let's do math with functions.")

age = add(13, 6)
height = subtract(78, 2)
weight = multiply(83, 2)
iq = divide(100, 2)

print(f"\nAge: {age}, \nHeight: {height}, \nWeight: {weight}, \nIQ: {iq}")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
print("That becomes: ", what, "Can you do it by hand?")
