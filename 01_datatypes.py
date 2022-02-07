name = input("what is your name?")
print("stored name : {}".format(name))

while True:
    try:
        age = int(input("how old are you?"))
        break
    except:
        print("<error> pleas enter your age")

