import sys
from sys import argv
from os.path import exists

script, from_file, to_file = argv

in_file = open(from_file.read())
#indata = in_file.read()
print(in_file)

