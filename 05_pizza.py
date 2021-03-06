
total_cost = 0.00
in_coupon = ""

crusts = ["thick crust", "thin crust"]
sizes = ["8 inch", "10 inch", "12 inch", "14 inch", "18 inch"]
cheeses = ["yes", "no"]
types = ["margarita", "vegetable", "vegan", "hawaiian", "meat feast"]
voucher_code = ["FunFriday"]

print("Welcome to pizza shack")

while True:
    order_crust = input("do you want thick or think crust? ").lower()
    if order_crust in crusts:
        break
    else:
        print("<error> pleas pick either \"{}\" or \"{}\"".format(crusts[0], crusts[1]))
        print("")
if order_crust == "thick crust":
    total_cost = total_cost + 8.00
else:
    total_cost = total_cost + 10.00

print("")

while True:
    order_size = input("would you like an 8, 10, 12, 14 or 18 inch pizza? ").lower()
    if order_size in sizes:
        break
    else:
        print("<error> pleas pick one of these sizes \"8 inch\", \"10 inch\", \"12 inch\", \"14 inch\", \"18 inch\"")
        print("")
if order_size == "8 inch" or order_size == "10 inch":
    total_cost = total_cost + 0.00
else:
    total_cost = total_cost + 2.00

print("")

while True:
    order_cheese = input("do you want cheese? ").lower()
    if order_cheese in cheeses:
        break
    else:
        print("<error> pleas put yes or no")
        print("")
if order_cheese == "no":
    total_cost = total_cost - 0.50

print("")

while True:
    order_type = input("what type of pizza would you like out of Margarita, Vegetable, Vegan, Hawaiian or Meat feast? ").lower()
    if order_type in types:
        break
    else:
        print("<error> pleas enter \"margarita\", \"vegetable\", \"vegan\", \"hawaiian\", \"meat feast\"")
        print("")
if order_type == types[1] or order_type == types[2]:
    total_cost = total_cost + 1.00
elif order_type == types[3] or order_type == types[4]:
    total_cost = total_cost + 2.00

print("")

while True:
    have_coupon = input("do you have a coupon/discount code").lower()
    if have_coupon == "no":
        break
    elif have_coupon == "yes":
        while True:
            in_coupon = input("what is you code (case sensitive)")
            if in_coupon in voucher_code:
                print("valid")
                break
            else:
                print("invalid")
                retry = input("do you want to retry").lower()
                if retry == "no":
                    break
                elif retry != "yes":
                    print("<error> please enter yes or no")
                    print("")
        break
    else:
        print("<error> please enter yes or no")
if in_coupon == voucher_code[0] and order_size == "18 inch":
    total_cost = total_cost - 2.00

print("")

if order_cheese == "yes":
    print("you ordered a {} {} pizza with a {} with cheese".format(order_size,order_type, order_crust))
    print("witch costs ${}".format(total_cost))
elif order_cheese == "no":
    print("you ordered a {} {} pizza with a {} without cheese".format(order_size,order_type, order_crust))
    print("witch costs ${}".format(total_cost))

print("thanks for ordering your order will arrive in the next few months")
