import sys
from os.path import exists
from sys import argv

script, fromfile, tofile = argv

print(f"Copying from {fromfile} to {tofile}")

infile = open(fromfile)
indata = infile.read()

print(indata)
print("The input file is", len(indata), "bytes long.")

print("Checking if the output file exists...")
existence = exists(tofile)


# If output file exists, prompt to overwrite.
if existence == True:
    print("File exists. Do you want to overwrite? (y/n)")
    overwrite = input('> ')
    if overwrite == 'n':
        print("Not overwriting. The script will now exit.")
        exit()

input("Press RETURN to continue, CTRL-C to abort: ")

outfile = open(tofile, 'w')
outfile.write(indata)

print("Successfully copied content from the old file to the new file.")
outfile.close()
infile.close()
