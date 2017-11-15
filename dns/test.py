import sys

array = 'hii', 'hi', 'sup', 'bye'
array2 = 'tes' 'tee' 'bah'
var1 = "hi"
var2 = "bye"

def func1(parameter1):
    if var1 == parameter1:
        return True
    else:
        return False



def func2():

    check = False
    for x in array:
        var = func1(x)
        if var == True:
            check = True
            break


    if check == False:
        print("No match.")


func2()
