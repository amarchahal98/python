print("""You enter a dark room with two doors. Do you go thorugh door 1 or 2?""")

door = input("> ")
if door == "1":
    print("big bear here eating cheesecake")
    print("What do you do?")
    print("1. Take the cake")
    print("2. Scream at the bear")

    bear = input("> ")

    if bear == "1":
        print("The bear eats your face off. GJ")
    elif bear == "2":
            print("The bear eats your legs off. GJ")
    else:
        print(f"Well, doing {bear} is probably better.")
        print("Bear runs away.")

elif door == "2":
    print("You stare into the endless abyss")
    print("1. Blueberries")
    print("2. Yellow jacket")
    print("3. Understanding revolvers yelling melodies")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.")
        print("GJ")
    else:
        print("The insanity rots your eyes")
        print("Good job!")

else:
    print("You stumble and fall")
