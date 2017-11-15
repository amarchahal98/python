# Common methods for files:
# close - Closes the file.
# read - Reads content of the file. Can assign the result to a var
# readline - Read one line of a text file
# truncate - Empties the file. Watch for this if file is important
# write('text') - Writes 'text' to the file
# seek(0) - Move the read/write location to beginning of the file
# Character for mode: w = write mode, r = read mode, a = append mode
# w+, r+, a+ = opens the file in both read/write, depending on character used

import sys
from sys import argv

scriptname, filename = argv

print(f"Erasing file:{filename} ")
input("Would you like to continue? (Enter = yes, Ctrl-C = Cancel?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. All content has been deleted from the file.")
target.truncate()

print("Input data for 3 more lines to add to the file.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("These lines will be written into the file.")

#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")


print("Done. Closing the file.")
target.close()

