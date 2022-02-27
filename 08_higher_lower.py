import random

number = random.randint(1,10)
players_guess = 0
lives = 3
guess = 0

print(number)
print("")

while players_guess != number and guess != lives:
    try:
        players_guess = int(input("guess the number between 1 and 10 "))
    except:
        print("<error> pleas enter a number")
        print("")
    if players_guess == number:
        print("nice you got it right")
    else:
        print("incorrect")
        guess = guess + 1
        print("you have {} lives left".format(lives - guess))
        if players_guess < number:
            print("the number is higher")
        else:
            print("the number is lower")
        print("")


if guess == lives:
    print("you ran out of lives better luck next time")
