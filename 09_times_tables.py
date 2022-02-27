
answer = 0

while True:
    try:
        times_table = int(input("what times tables do you want"))
        break
    except:
        print("<error> enter a number")
        print("")

print("")

print('here is the {} times table'.format(times_table))
for x in range(1,13):
    answer = x * times_table
    print("{} times {} is {}".format(x,times_table, answer))
