import sys

var = sys.argv[1]

def myfunc(parameter):
    if parameter < 5:
        print("value low value")
    
    if parameter == 5:
        print("correct value")

    if parameter > 5:
        print("value too high")


myfunc(int(var))
