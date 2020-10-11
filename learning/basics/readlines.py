#!/usr/bin/python3
# Test function of f.readlines() (Note, not readline)

file = open("textfile.txt")

for line in file.readlines():
    print(line)

file.close()

