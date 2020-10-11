import sys

#var = sys.argv[1]

def myfunc(parameter):
    if parameter < 5:
        print("low value: " + str(parameter))
    
    if parameter == 5:
        print("correct value: " + str(parameter))

    if parameter > 5:
        print("high value: " + str(parameter))


# myfunc(int(var))
for arg in sys.argv[1:]:
    num = int(arg)
    myfunc(num)
