#!/usr/bin/python3
# Asking Questions - Using input

print("How old are you?", end='  ')
age = int(input())
print("How tall are you?",  end='  ')
height = input()
print("How much do you weigh?", end='  ')
weight = input()

print(f"So you're {age} years old, {height} tall and {weight} heavy.")
print("In 5 years from now, you will be", (age + 5), "years old.")
