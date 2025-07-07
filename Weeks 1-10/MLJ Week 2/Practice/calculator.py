# Calculator! 
# Simlple arithmetic calculator.
# 
# Joshua Fashe
# 7/7/2025 3:57am
# calculator.py

arithmetic = input("Would you like to add, subtract, multiply or divide? ").lower()
x = int(input("Enter your first number: "))
y = int(input("Enter your second number: "))
match arithmetic:
    case "1" | "+" | "add" | "addition" :
        print(f"{x} + {y} = {x+y}")
    case "2" | "-" | "subtract" | "subtraction" :
        print(f"{x} - {y} = {x-y}")
    case "3" | "*" | "multiply" | "multiplication" :
        print(f"{x} * {y} = {x*y}")
    case "4" | "/" | "divide" | "division" :
        print(f"{x} / {y} = {x/y}")
    case _:
        print("Unknown arithmetic type.")


#finished 4:07am