
name = input("what is your name? ").lower()

if name == "anakin":
    print("how do you do anakin!")
elif name == "leia":
    print("may the force be with you")
else:
    print("nice name, {}".format(name))

weather = input("so {}, is it hot or cold where you are today? ".format(name)).upper()
if weather == "COLD":
    print("you must be freezing!")
elif weather == "HOT":
    print("drink plenty of water")
else:
    print("i can't advise you on that type of weather")

likes_blue = input("do you like the colour blue? ").upper()
if likes_blue == "YES":
    print("i like blue too")
else:
    print("That’s a shame because I really like blue")

print("have a good day, bye")
