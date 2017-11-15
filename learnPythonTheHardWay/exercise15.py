from sys import argv

script, filename = argv

txt = open(filename)

print("File: " + filename)
print(txt.read())


