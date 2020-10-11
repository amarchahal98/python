#!/usr/bin/python3
# Exercise 8 - More complicated String Formatting

formatter = "{} {} {} {}"
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))

print(formatter.format(
    "I can not",
    "think of",
    "anything to write",
    "so I'll leave this here."
))
