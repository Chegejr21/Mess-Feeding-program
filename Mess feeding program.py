print("WELCOME TO TTU MESS...:")
name = input("Enter your name:")
print("Hey there! " + name, "You can now order your favourite dish and drink as well")
time = int(input("Enter time of the day.... 0600 hrs to 2100 hrs:"))
if time >= 6 and time <= 11:
    print("Good morning " + name, "Its breakfast time...make your order:")
    drinks = input(["coffee", "yoghurt", "tea", "soda", "milk"])
    if drinks == "coffee":
        print("You ordered coffee @ 20 Ksh")
    elif drinks == "tea":
        print("You ordered tea @ 10 Ksh")
    elif drinks == "yoghurt":
        print("You ordered yoghurt @ 70 Ksh")
    elif drinks == "soda":
        print("You ordered soda @ 40 Ksh")
    elif drinks == "milk":
        print("You ordered milk @ 30 Ksh")
    else:
        print("Ooops! Invalid drink request")
elif time >= 12 and time <= 17:
    print("Good afternoon " + name, "Its lunch time...make your order:")
    importdrinks = input(["coffee", "yoghurt", "tea", "soda", "milk"])
    dish_choices = input(["chapo and beans", "chapo and pojo", "rice and beans", "rice and pojo", "ugali and matumbo", "ugali and mayai", "pilau", "githeri"])
    if dish_choices == "chapo and beans":
        print("You ordered chapo and beans @ Kshs 60")
    elif dish_choices == "chapo and pojo":
        print("You ordered chapo pojo @ Ksh 60")
    elif dish_choices == "rice and beans":
        print("You ordered rice and beans @ kshs 50")
    elif dish_choices == "rice and pojo":
        print("You ordered rice and pojo @ Kshs 50")
    elif dish_choices == "ugali and matumbo":
        print("You ordered ugali and matumbo @ Kshs 80")
    elif dish_choices == "ugali and mayai":
        print("You ordered ugali and mayai @ Kshs 65")
    elif dish_choices == "pilau"
        print("You ordered pilau @ Kshs 100")
    elif dish_choices == "githeri":
        print("You ordered githeri @ Kshs")
    else:
        print("Invalid food request")
elif time >= 18 and time <= 21:
    print("Good evening " + name, "Its supper time...make your order")
    importdrinks = input(["coffee", "yoghurt", "tea", "soda", "milk"])
    dish_choices = input(["chapo and beans", "chapo and pojo", "rice and beans", "rice and pojo", "ugali and matumbo", "ugali and mayai", "pilau", "githeri"])
    if dish_choices == "chapo and beans":
        print("You ordered chapo and beans @ Kshs 60")
    elif dish_choices == "chapo and pojo":
        print("You ordered chapo pojo @ Ksh 60")
    elif dish_choices == "rice and beans":
        print("You ordered rice and beans @ kshs 50")
    elif dish_choices == "rice and pojo":
        print("You ordered rice and pojo @ Kshs 50")
    elif dish_choices == "ugali and matumbo":
        print("You ordered ugali and matumbo @ Kshs 80")
    elif dish_choices == "ugali and mayai":
        print("You ordered ugali and mayai @ Kshs 65")
    elif dish_choices == "pilau":
        print("You ordered pilau @ Kshs 100")
    elif dish_choices == "githeri":
        print("You ordered githeri @ Kshs")
    else:
        print("Invalid food request")
else:
    print("You are late")