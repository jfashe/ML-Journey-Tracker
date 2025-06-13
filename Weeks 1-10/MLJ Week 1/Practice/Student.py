# Welcome to build-a-human workshop, lets make a student?
import time
answer1 = input("Hi! How are you!",)

if answer1[0].lower() == 'g': # If the answer starts with a 'g' (like Good or Great)
    print("Glad to hear! What can I get for you?")
else:
    print("Sucks to suck. What do you want to make?")

time.sleep(1)
choice = input("enter 'a' to make a student, 'b' to marry a couple, and 'c' to... idk...")
match choice:
    case "a":
        student={
            "name":input("Student name? "),
            "age":int(input("Student age? ")),
            "GPA":float(input("Student GPA? ")),
            }ß
    case "b":
        husband = input("Enter the husbands FULL name: ")
        while " " in husband:
            husband_first,husband_last = husband.split(" ")
            input(f"Is {husband_last} the last name?")