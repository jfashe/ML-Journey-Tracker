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
        gender = input("\"His\" or \"Her\"?")

        student={
            "name":input("Student name? "),
            "school":input("Student school? "),
            "age":int(input("Student age? ")),
            "GPA":float(input("Student GPA? ")),
            }
        print("loading..."), time.sleep(1)
        print(f"Got it! {gender} name is {student["name"]}. A beautiful student at {student["school"]}, with a {student["gpa"]} GPA!")
    case "b":
        husband = input("Enter the husbands FULL name: ")
        while " " in husband:
            husband_first,husband_last = husband.split(" ")
            input(f"Is {husband_last} the last name?")