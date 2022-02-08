print("wlecome to SPILT MY PIZZA")
print("where we split yor pizza for free")
print("")

while True:
    try:
        slicers = int(input("how many slicers of pizza do you want? "))
        break
    except:
        print("<error> pleas enter a number"
              "")

print("")

while True:
    try:
        people = int(input("how many people will be splitting the pizza? "))
        break
    except:
        print("<error> pleas enter a number")
        print("")

slicers_per_people = people//slicers
left_over_slicers = people%slicers

print("")
print("so each person will get {} slice" .format(slicers_per_people))
print("and there will be {} slicers left over".format(left_over_slicers))
print("")
print("thanks for splitting your pizza with")
print("SPLIT MY PIZZA")
