# https://video.cs50.io/JP7ITIXGpHk
# Functions - Definitions, Parameters, AND Return Values

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