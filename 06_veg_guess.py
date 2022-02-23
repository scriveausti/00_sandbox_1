
YesNo = ["y", "n"]

def yes_no_question(q):
    while True:
        answer = input(q).lower()
        if answer in YesNo:
            break
        else:
            print("<error> pleas enter \"y\" or \"n\"")
    return answer

print("pick either Peas, Broccoli, Carrot or Sweetcorn")
print("I will attempt to guess your choice")

question = "is it green? Y/N "
answer = yes_no_question(question)
if answer == "n":
    answer = yes_no_question("is it orange? Y/N ")
    if answer == "y":
        print("it must be an carrot!")
    else:
        print("it must be sweetcorn!")

else:
    question = "does it look like a tree? Y/N "
    answer = yes_no_question(question)
    if answer == "n":
        print("it must be a pea then!")
    else:
        print("it must be broccoli then!")
