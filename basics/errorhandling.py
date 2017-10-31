while True:
    try:
        number = int(input("enter a number: "))
        break
    except TypeError:
        print("That is not a number.")


