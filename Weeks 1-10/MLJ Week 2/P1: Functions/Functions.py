# https://video.cs50.io/JP7ITIXGpHk - CS50P Week0, Functions
# Functions - Definitions, Parameters, AND Return Values
# CS50 was good, don't get me wrong, but Bro Code summarizes all three in just 10 minutes here:
# https://www.youtube.com/watch?v=89cGQjB5R4M

def greet_name(name = "Joshua"):
    # takes an input (name), sets default parameter to string "joshua".
    return f"Hello, {name}"
    # return value is an fstring, "hello, (name)"

print(greet_name()) # no parameter inputted, defers to original parameter 

my_name = input("what's your name? ")
print(greet_name(my_name))
# prints the return value of function greetname()


# GOOD PRACTICE
def greet_name2(name: str) -> str:
    # takes an input (name), but HINTS that the parameter should be a str (string).
    return(f"Hello, {name}")
    # return value is an fstring, "hello, (name)"