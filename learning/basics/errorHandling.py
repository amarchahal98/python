import sys

while True:
    try:
        var = sys.argv[1]
        break
    except IndexError:
        print("No value given.")
        sys.exit()

while True:
    try:
        number = int(var)
        break
    except ValueError:
        print("Incorrect input")
        break


