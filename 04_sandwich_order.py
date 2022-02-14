
total_cost = 0.00
suger_tax = 0.50

bread_type = input("sandwich or wrap? ").lower()
filling_type = input("meat, vegetarian or vegan? ").lower()
pudding = input("cookie, chips, fruit or none ").lower()
drink = input("fizzy drink, water or none? ").lower()
extra_sauce = input("would you like extra sauce? ").lower()
extra_salad = input("do you want extra salad? ").lower()

if bread_type != "sandwich":
    total_cost = 2.00
else:
    total_cost = 3.00

if filling_type == "vegetarian" or filling_type == "vegan":
    total_cost = total_cost + 1.00
else:
    total_cost = total_cost + 1.50

if pudding == "cookie" and drink == "fizzy drink":
    total_cost = total_cost + suger_tax
if pudding == "none" or drink == "none":
    total_cost = total_cost - 0.50
if extra_salad == "yes" and extra_sauce =="yes":
    total_cost = total_cost + 1.00

print("your total cost is: ${}".format(total_cost))
