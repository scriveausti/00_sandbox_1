while True:
    name = input("what is your name?")
    if name == "":
        print("")
        print("pleas enter your name")
    else:
        break
print("")
print("stored name : {}".format(name))

print("")
while True:
    try:
        age = int(input("how old are you?"))
        break
    except:
        print("")
        print("<error> pleas enter your age")
print("")
print("stored age : {}".format(age))
