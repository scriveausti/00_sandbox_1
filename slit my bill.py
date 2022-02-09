cost_of_slice = 1.50

print("Welcome to SPILT MY PIZZA")
print("where we split yor pizza for free")
print("")

while True:
    try:
        slicers = int(input("how many slicers of pizza do you want? "))
        break
    except:
        print("<error> pleas enter the number of slicers you want"
              "")

print("")

while True:
    try:
        people = int(input("how many people will be splitting the slicers? "))
        break
    except:
        print("<error> pleas enter the number of people splitting the slicers ")
        print("")

cost_of_slice_all = slicers*cost_of_slice

print("")
print("the total cost of the slices is ${}".format(cost_of_slice_all))
print("")

while True:
    try:
        people_splitting_bill = int(input("how many people will be splitting the bill "))
        break
    except:
        print("<error> pleas enter the number of people splitting the bill")
        print("")

print("")

while True:
    try:
        tip_percentage = int(input("what percentage would you like to tip "))
        break
    except:
        print("<error> pleas enter the percentage you would like to tip e.g. \"20\"")
        print("")


slicers_per_people = slicers//people
left_over_slicers = slicers%people
tip_percentage = tip_percentage/100
tip = cost_of_slice_all*tip_percentage
total_cost = cost_of_slice_all + tip
cost_each = total_cost/people_splitting_bill

print("")
print("so each person will get {} slice" .format(slicers_per_people))
print("and there will be {} slicers left over".format(left_over_slicers))
print("")
print("the total cost it ${} split among {} people".format(total_cost,people_splitting_bill))
print("so each person pays ${}".format(cost_each))
print("")
print("thanks for splitting your pizza with")
print("SPLIT MY PIZZA")
