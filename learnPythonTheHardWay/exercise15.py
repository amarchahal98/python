#!/usr/bin/python3
# Exercise 15 - Reading Files - use textfile as arg

from sys import argv

script, filename = argv

txt = open(filename)

print("File: " + filename)
print(txt.read())

txt.close()

print("Type the filename again: ")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())

txt_again.close()
