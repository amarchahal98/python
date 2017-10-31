x = 3

# (Negate value x. also works with +) Evaluation: 2
#print(-x + 5)

y = -5
# (Absolute value of y) Evaluation: 5
#print(abs(y))

z = 125
# (Prints value in binary format)
#print(bin(z))

strA = "google"
strB = "go123"

def searchFunc(contains):
    try:
        if strA.index(contains) == True:
            print("A")
    except ValueError:
        print("The input '" + contains + "' is not permitted")

#searchFunc(strB)

## str.startswith/str.endswith ##

ip = '192.168.0.1'
internaldomain = "192.168."
if ip.startswith(internaldomain):
    print("LAN IP")
else:
    print("Foreign IP")


